from __future__ import annotations
from pathlib import Path
import json

# JSON is the single source of truth (editable without code changes)
JSON_PATH = Path(__file__).with_name("system_prompts.json")

# Fallback defaults (only used if JSON missing/broken)
_FALLBACK_PRESETS = [
    "📝 Enhance",
    "📝 Refine",
    "📝 Creative Rewrite",
    "📝 Detailed Visual",
    "📝 Artistic Style",
    "📝 Technical Specs",
]

_FALLBACK_SYSTEM_PROMPTS = {
    "📝 Enhance": "You are a professional photography prompt writer. Output ONLY the improved prompt."
}

# token defaults (can also be moved into JSON later if you want)
PRESET_TOKEN_DEFAULTS = {k: 700 for k in _FALLBACK_PRESETS}

def _load_json():
    if not JSON_PATH.exists():
        return None
    try:
        return json.loads(JSON_PATH.read_text(encoding="utf-8"))
    except Exception:
        return None

data = _load_json()

if data:
    PRESET_PROMPTS = list(data.get("_preset_prompts") or _FALLBACK_PRESETS)
    # We read qwen_text/styles/<preset>/system_prompt
    styles = (((data.get("qwen_text") or {}).get("styles")) or {})
    SYSTEM_PROMPTS = {}
    for k in PRESET_PROMPTS:
        v = ((styles.get(k) or {}).get("system_prompt"))
        if isinstance(v, str) and v.strip():
            SYSTEM_PROMPTS[k] = v
    # Ensure at least fallback for missing ones
    for k in PRESET_PROMPTS:
        SYSTEM_PROMPTS.setdefault(k, _FALLBACK_SYSTEM_PROMPTS.get(k, _FALLBACK_SYSTEM_PROMPTS["📝 Enhance"]))
    # Token defaults per preset (from JSON), with fallback to defaults.max_tokens
    PRESET_TOKEN_DEFAULTS = {}
    default_max = int((data.get("defaults") or {}).get("max_tokens") or 700)
    for k in PRESET_PROMPTS:
        mt = ((styles.get(k) or {}).get("max_tokens"))
        try:
            PRESET_TOKEN_DEFAULTS[k] = int(mt) if mt is not None else default_max
        except Exception:
            PRESET_TOKEN_DEFAULTS[k] = default_max

else:
    PRESET_PROMPTS = _FALLBACK_PRESETS
    SYSTEM_PROMPTS = _FALLBACK_SYSTEM_PROMPTS
    PRESET_TOKEN_DEFAULTS = {k: 700 for k in PRESET_PROMPTS}
