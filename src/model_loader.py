"""统一模型加载器：按顺序尝试下载源，按重试次数回退。"""

from __future__ import annotations

from contextlib import contextmanager
import os
import time
from typing import Callable, Optional

from sentence_transformers import SentenceTransformer


HUGGINGFACE_ENDPOINT = "https://huggingface.co"
MODELSCOPE_ENDPOINT = "https://modelscope.cn/hf"
_DEFAULT_RETRIES = 3
_DEFAULT_HF_BACKOFF_RETRIES = 1


def _log_default(message: str) -> None:
  print(message, flush=True)


@contextmanager
def _hf_http_backoff(max_retries: int):
  """临时覆盖 huggingface_hub 的 http_backoff 重试次数。

  仅用于抑制单次请求内置重试次数（日志中通常体现为 `Retry x/5`）。
  """
  if max_retries <= 0:
    yield
    return

  try:
    from huggingface_hub.utils import _http as hf_http
  except Exception:
    yield
    return

  origin_http_backoff = hf_http.http_backoff

  def http_backoff_with_retry_limit(*args, **kwargs):
    kwargs.setdefault("max_retries", max_retries)
    return origin_http_backoff(*args, **kwargs)

  hf_http.http_backoff = http_backoff_with_retry_limit
  try:
    yield
  finally:
    hf_http.http_backoff = origin_http_backoff


@contextmanager
def _hf_endpoint(endpoint: Optional[str] = None):
  had_endpoint = "HF_ENDPOINT" in os.environ
  old_endpoint = os.environ.get("HF_ENDPOINT")
  had_base_url = "HF_HUB_BASE_URL" in os.environ
  old_base_url = os.environ.get("HF_HUB_BASE_URL")
  if endpoint:
    os.environ["HF_ENDPOINT"] = endpoint
    os.environ["HF_HUB_BASE_URL"] = endpoint
  elif had_endpoint:
    if "HF_ENDPOINT" in os.environ:
      del os.environ["HF_ENDPOINT"]
    if "HF_HUB_BASE_URL" in os.environ:
      del os.environ["HF_HUB_BASE_URL"]

  try:
    yield
  finally:
    if had_endpoint:
      if old_endpoint is None:
        del os.environ["HF_ENDPOINT"]
      else:
        os.environ["HF_ENDPOINT"] = old_endpoint
    elif "HF_ENDPOINT" in os.environ:
      del os.environ["HF_ENDPOINT"]
    if had_base_url:
      if old_base_url is None:
        del os.environ["HF_HUB_BASE_URL"]
      else:
        os.environ["HF_HUB_BASE_URL"] = old_base_url
    elif "HF_HUB_BASE_URL" in os.environ:
      del os.environ["HF_HUB_BASE_URL"]


def load_sentence_transformer(
  model_name: str,
  *,
  device: str,
  retries: int | None = None,
  log: Callable[[str], None] = _log_default,
  providers: tuple[tuple[str, str], ...] = (
    ("huggingface", HUGGINGFACE_ENDPOINT),
    ("modelscope", MODELSCOPE_ENDPOINT),
  ),
):
  if retries is None:
    env_retries = os.getenv("LLM_EMBED_MODEL_RETRIES")
    if env_retries is None:
      retries = _DEFAULT_RETRIES
    else:
      try:
        retries = int(env_retries)
      except ValueError:
        print(f"[WARN] 环境变量 LLM_EMBED_MODEL_RETRIES 无效：{env_retries}，回退默认 {_DEFAULT_RETRIES}")
        retries = _DEFAULT_RETRIES
  hf_backoff_retries = _DEFAULT_HF_BACKOFF_RETRIES
  env_hf_backoff_retries = os.getenv("HF_HUB_HTTP_BACKOFF_RETRIES")
  if env_hf_backoff_retries is not None:
    try:
      hf_backoff_retries = int(env_hf_backoff_retries)
    except ValueError:
      print(
        f"[WARN] 环境变量 HF_HUB_HTTP_BACKOFF_RETRIES 无效：{env_hf_backoff_retries}，"
        f"回退默认 {_DEFAULT_HF_BACKOFF_RETRIES}"
      )
      hf_backoff_retries = _DEFAULT_HF_BACKOFF_RETRIES
    if hf_backoff_retries < 0:
      hf_backoff_retries = 0

  attempts = max(int(retries or _DEFAULT_RETRIES), 1)
  last_err: Exception | None = None

  for round_idx in range(1, attempts + 1):
    for provider_name, endpoint in providers:
      try:
        log(
          f"[INFO] 尝试加载模型（第 {round_idx}/{attempts} 轮）：{model_name}"
          f"（provider={provider_name}，device={device}）"
        )
        with _hf_endpoint(endpoint), _hf_http_backoff(max_retries=hf_backoff_retries):
          return SentenceTransformer(model_name, device=device)
      except Exception as e:  # pragma: no cover - 仅异常路径
        last_err = e
        msg = str(e)
        if len(msg) > 260:
          msg = msg[:260]
        log(
          f"[WARN] 模型加载失败（provider={provider_name}，round={round_idx}/{attempts}）："
          f"{msg}"
        )

    if round_idx < attempts:
      wait_seconds = 1
      log(f"[INFO] 重试间隔：{wait_seconds}s")
      time.sleep(wait_seconds)

  if last_err is not None:
    raise last_err
  raise RuntimeError(f"加载模型失败：{model_name}")
