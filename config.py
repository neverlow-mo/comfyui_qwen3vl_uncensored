"""Qwen3-VL Uncensored - Config FIXED"""
import os
from pathlib import Path

LLAMA_CLI = Path.home() / "ai" / "llama-cpp-core" / "build" / "bin" / "llama-cli"
MODEL_PATH = Path("/mnt/popbackup/ai/comfyui-models/models/LLM/GGUF/Qwen3-VL-30B-abliterated-Q4/huihui-qwen3-vl-30b-a3b-instruct-abliterated-q4_k_m.gguf")
MMPROJ_PATH = Path("/mnt/popbackup/ai/comfyui-models/models/LLM/GGUF/Qwen3-VL-30B-abliterated-Q4/Qwen3-VL-30B-A3B-Instruct-abliterated.mmproj-f16.gguf")

N_GPU_LAYERS = 99
CONTEXT_SIZE = 8192
MAX_TOKENS = 500
TEMPERATURE = 0.7

# KÜRZERE System-Prompts (unter 500 tokens!)
SYSTEM_PROMPT_ENHANCE = """You are a Stable Diffusion prompt expert. Enhance the user's prompt with visual details, lighting, style, and quality keywords. Answer ONLY with the enhanced prompt, NO explanations."""

SYSTEM_PROMPT_DESCRIBE = """Analyze this image and create a Stable Diffusion prompt describing all visual elements. Include composition, lighting, colors, and technical details. Answer ONLY with the prompt."""

def validate_config():
    errors = []
    if not LLAMA_CLI.exists():
        errors.append(f"❌ llama-cli: {LLAMA_CLI}")
    if not MODEL_PATH.exists():
        errors.append(f"❌ Model: {MODEL_PATH}")
    if not MMPROJ_PATH.exists():
        errors.append(f"⚠️ MMProj: {MMPROJ_PATH}")
    return errors

if __name__ != "__main__":
    _errors = validate_config()
    if _errors:
        print("\n".join(_errors))
