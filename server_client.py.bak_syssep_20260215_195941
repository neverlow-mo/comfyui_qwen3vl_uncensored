from __future__ import annotations

import base64
import json
import urllib.request
import urllib.error
from pathlib import Path


DEFAULT_SERVER_URL = "http://127.0.0.1:8089"


def _post_json(url: str, payload: dict, timeout: int = 180) -> dict:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def chat_completions(
    *,
    server_url: str = DEFAULT_SERVER_URL,
    model: str,
    system: str = "",
    user: str,
    image_path: str | None = None,
    max_tokens: int | None = None,
    temperature: float = 0.7,
    seed: int | None = None,
) -> str:
    url = server_url.rstrip("/") + "/v1/chat/completions"

    messages: list[dict] = []
    if system:
        messages.append({"role": "system", "content": system})

    if image_path:
        data = Path(image_path).read_bytes()
        b64 = base64.b64encode(data).decode("ascii")
        messages.append(
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
                ],
            }
        )
    else:
        messages.append({"role": "user", "content": user})

    payload: dict = {
        "model": model,
        "messages": messages,
        "temperature": float(temperature),
    }
    if max_tokens is not None:
        payload["max_tokens"] = int(max_tokens)
    if seed is not None:
        payload["seed"] = int(seed)

    data = _post_json(url, payload)

    content = data["choices"][0]["message"]["content"]
    if isinstance(content, list):
        content = "\n".join([c.get("text", "") for c in content if isinstance(c, dict)])
    return (content or "").strip()
