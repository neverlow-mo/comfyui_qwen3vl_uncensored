"""
Qwen3-VL Uncensored - llama.cpp Wrapper
========================================
Version: 5.0 ULTIMATE - Capture stdout AND stderr!
"""

import subprocess
import tempfile
from pathlib import Path
from typing import Optional

from . import config


class LlamaWrapper:
    """Interface zu llama.cpp"""
    
    def __init__(self):
        self.llama_cli = config.LLAMA_CLI
        self.model = config.MODEL_PATH
        self.mmproj = config.MMPROJ_PATH
        
        if not self.llama_cli.exists():
            raise FileNotFoundError(f"llama-cli nicht gefunden: {self.llama_cli}")
        if not self.model.exists():
            raise FileNotFoundError(f"Modell nicht gefunden: {self.model}")
    
    def generate(
        self, 
        prompt: str,
        image_path: Optional[Path] = None,
        system_prompt: Optional[str] = None,
        max_tokens: int = config.MAX_TOKENS,
        temperature: float = config.TEMPERATURE
    ) -> str:
        """Generiert eine Antwort vom Modell"""
        
        if system_prompt:
            full_prompt = f"{system_prompt}\n\nUser: {prompt}\n\nAssistant:"
        else:
            full_prompt = prompt
        
        cmd = [
            str(self.llama_cli),
            "-m", str(self.model),
            "-p", full_prompt,
            "-n", str(max_tokens),
            "-ngl", str(config.N_GPU_LAYERS),
            "-c", str(config.CONTEXT_SIZE),
            "--temp", str(temperature),
            "-st",
        ]
        
        if image_path and self.mmproj.exists():
            cmd.extend(["--mmproj", str(self.mmproj)])
            cmd.extend(["--image", str(image_path)])
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=120,
                check=True
            )
            
            # WICHTIG: Kombiniere stdout UND stderr!
            # llama-cli gibt interaktiven Output über stderr aus!
            combined_output = result.stdout + "\n" + result.stderr
            
            response = self._extract_response(combined_output)
            
            return response
            
        except subprocess.TimeoutExpired:
            return "❌ ERROR: Timeout (>2 Min)"
        except subprocess.CalledProcessError as e:
            return f"❌ ERROR: llama-cli Fehler:\n{e.stderr}"
        except Exception as e:
            return f"❌ ERROR: {str(e)}"
    
    def _extract_response(self, output: str) -> str:
        """
        Extrahiert die Antwort zwischen '>' (Prompt-Echo) und '[' (Performance)
        """
        
        lines = output.split('\n')
        
        # Finde letzte Zeile die mit '>' beginnt
        prompt_echo_idx = -1
        for i, line in enumerate(lines):
            if line.strip().startswith('>'):
                prompt_echo_idx = i
        
        # Finde erste Zeile mit Performance-Info
        perf_line_idx = len(lines)
        for i, line in enumerate(lines):
            if line.strip().startswith('[') and 't/s' in line:
                perf_line_idx = i
                break
        
        # Extrahiere Antwort
        if prompt_echo_idx >= 0:
            response_lines = lines[prompt_echo_idx + 1:perf_line_idx]
        else:
            response_lines = lines[:perf_line_idx]
        
        # Entferne leere Zeilen
        response_lines = [l for l in response_lines if l.strip() and not l.strip().startswith('llama_') and not l.strip().startswith('ggml_')]
        
        response = '\n'.join(response_lines).strip()
        
        # Entferne "Exiting..." falls am Ende
        if response.endswith('Exiting...'):
            response = response[:-10].strip()
        
        if not response:
            print(f"[LlamaWrapper] ERROR: Empty response after extraction!")
            print(f"[LlamaWrapper] Output length: {len(output)} chars")
            print(f"[LlamaWrapper] Output preview (first 1000 chars):\n{output[:1000]}")
            response = "❌ ERROR: Antwort konnte nicht extrahiert werden"
        
        return response
    
    def enhance_prompt(self, text_prompt: str) -> str:
        """Verbessert einen Text-Prompt"""
        return self.generate(
            prompt=text_prompt,
            system_prompt=config.SYSTEM_PROMPT_ENHANCE,
            max_tokens=300,
            temperature=0.7
        )
    
    def describe_image(self, image_path: Path) -> str:
        """Beschreibt ein Bild"""
        if not image_path.exists():
            return f"❌ ERROR: Bild nicht gefunden: {image_path}"
        
        return self.generate(
            prompt="Describe this image and create a Stable Diffusion prompt.",
            image_path=image_path,
            system_prompt=config.SYSTEM_PROMPT_DESCRIBE,
            max_tokens=400,
            temperature=0.6
        )
    
    def multimodal_enhance(self, text_prompt: str, image_path: Path) -> str:
        """Kombiniert Bild + Text"""
        if not image_path.exists():
            return f"❌ ERROR: Bild nicht gefunden: {image_path}"
        
        combined_system = f"""{config.SYSTEM_PROMPT_DESCRIBE}

The user provides both a text prompt AND a reference image.
Your task: Combine both to create an enhanced Stable Diffusion prompt.
"""
        
        return self.generate(
            prompt=f"Text: {text_prompt}",
            image_path=image_path,
            system_prompt=combined_system,
            max_tokens=500,
            temperature=0.7
        )
