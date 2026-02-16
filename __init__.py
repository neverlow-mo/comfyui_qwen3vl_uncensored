"""
Qwen3-VL Uncensored - ComfyUI Node Registration
================================================
Registriert den Node in ComfyUI

Autor: Martin + Claude Coach
Datum: 2026-02-13
"""

from .qwen3vl_node import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# ComfyUI erwartet diese Variablen
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

# Startup-Nachricht
print("\n" + "="*70)
print("🔓 Qwen3-VL Prompt Generator (Uncensored) loaded!")
print("   - Text Enhancement: ✅")
print("   - Image Description: ✅")  
print("   - Multimodal: ✅")
print("   - Zensurfrei: ✅")
print("   - RTX 5090 optimiert: ✅")
print("="*70 + "\n")

# Validiere Config beim Import
from . import config

errors = config.validate_config()
if errors:
    print("⚠️  CONFIG WARNINGS:")
    for error in errors:
        print(f"   {error}")
    print()
