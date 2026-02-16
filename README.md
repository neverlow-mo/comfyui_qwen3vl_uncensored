# ComfyUI Qwen3-VL Prompt Generator (Uncensored)

A ComfyUI custom node that generates/refines prompts using a local Qwen3-VL/llama.cpp backend (CLI or llama-server), with editable **system prompts** and **per-preset max_tokens** via JSON.

## Features
- Prompt enhancement presets (system prompts stored in `system_prompts.json`)
- Per-preset `max_tokens` defaults (also from JSON)
- Works offline with local inference
- CLI fallback if llama-server is not reachable
- Output cleanup (spinner/control chars)

## Install (manual)
1. Copy/clone into your ComfyUI `custom_nodes/` folder:
   - Folder name: `comfyui_qwen3vl_uncensored`
2. Restart ComfyUI.

## Configure presets / personality
Edit:
- `system_prompts.json`

You can define:
- `_preset_prompts` (order shown in UI)
- `qwen_text.styles.<preset>.system_prompt`
- `qwen_text.styles.<preset>.max_tokens`
- `defaults.max_tokens`

## Security / Privacy
- No API keys required.
- Runs locally.
- Check code before use (recommended).

## Troubleshooting
- If you see `llama-server not reachable`, the node will fall back to CLI automatically.
- If a JSON edit breaks parsing, restore from the `.bak_*.json` backup or fix syntax.

## License
MIT (see `LICENSE`).
