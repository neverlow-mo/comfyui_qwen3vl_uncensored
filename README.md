# Qwen3-VL Prompt Generator (Uncensored) 🔓

**ComfyUI Custom Node** für zensurfreie Prompt-Generierung mit Qwen3-VL-30B

---

## 🎯 Features

- ✅ **Text Enhancement**: Verbessert einfache Prompts → detaillierte SD-Prompts
- ✅ **Image Description**: Analysiert Bilder → generiert Prompts
- ✅ **Multimodal**: Kombiniert Text + Bild → optimierte Prompts
- ✅ **Zensurfrei**: Ablitiertes Modell (keine Content-Filter!)
- ✅ **RTX 5090 optimiert**: ~225 t/s Generation-Speed
- ✅ **30B Parameter**: Sehr intelligente Prompt-Generierung

---

## 📦 Installation

### 1. Voraussetzungen

- ✅ llama.cpp kompiliert (mit CUDA)
- ✅ Qwen3-VL-30B-abliterated-Q4_K_M GGUF-Modell
- ✅ MMProj-File (für Vision)

### 2. Installation

```bash
cd ~/ai/comfy-cu130/custom_nodes/
git clone <dein-repo> comfyui-qwen3vl-uncensored
# ODER kopiere den Ordner manuell
```

### 3. Konfiguration

Passe `config.py` an:

```python
LLAMA_CLI = Path.home() / "ai" / "llama-cpp-core" / "build" / "bin" / "llama-cli"
MODEL_PATH = Path("/pfad/zu/deinem/modell.gguf")
MMPROJ_PATH = Path("/pfad/zu/deinem/mmproj.gguf")
```

### 4. ComfyUI neu starten

Der Node erscheint unter: **Add Node → prompt → qwen3vl**

---

## 🎬 Nutzung

### Mode 1: **enhance** (Text → Enhanced Text)

```
Input:  "a cat"
Output: "a majestic fluffy cat, sitting on windowsill, golden hour lighting, 
         photorealistic, highly detailed fur texture, bokeh background, 
         professional photography, 8k uhd, masterpiece, best quality"
```

**Use Case**: Verbessere kurze/einfache Prompts

---

### Mode 2: **describe** (Image → Prompt)

```
Input:  [Bild einer Landschaft]
Output: "breathtaking mountain landscape, snow-capped peaks, crystal clear lake 
         in foreground, dramatic clouds, sunset lighting, wide angle shot, 
         vibrant colors, highly detailed, masterpiece, 8k"
```

**Use Case**: Erstelle Prompts aus Referenzbildern

---

### Mode 3: **multimodal** (Text + Image → Enhanced Prompt)

```
Input Text:  "make it cyberpunk"
Input Image: [Stadtbild]
Output:      "futuristic cyberpunk cityscape, neon lights, holographic billboards, 
              rain-soaked streets, night scene, dark atmosphere, blade runner style, 
              highly detailed, cinematic lighting, 8k uhd, masterpiece"
```

**Use Case**: Kombiniere deine Idee mit einem Referenzbild

---

## ⚙️ Parameter

| Parameter | Beschreibung | Default |
|-----------|--------------|---------|
| `mode` | enhance / describe / multimodal | enhance |
| `text` | Text-Prompt (optional je nach Mode) | - |
| `image` | Bild (optional je nach Mode) | - |
| `temperature` | Kreativität (0.0 = deterministisch, 1.0 = kreativ) | 0.7 |
| `max_tokens` | Maximale Antwort-Länge | 400 |

---

## 🔒 Zensurfreiheit

Dieses Node nutzt ein **ablitiertes** (uncensored) Modell.

**Was das bedeutet:**
- ✅ Keine Content-Filter
- ✅ Beschreibt objektiv, was du anforderst
- ✅ Kein "I cannot help with that"
- ✅ Für professionelle/künstlerische Nutzung

**Verantwortung**: Du bist für die Nutzung verantwortlich!

---

## 🚀 Performance

**Hardware**: RTX 5090 (32GB VRAM)  
**Modell**: Qwen3-VL-30B Q4_K_M  
**Speed**: ~225 t/s Generation  
**VRAM**: ~19GB (bleibt 13GB frei)

**Schneller als die meisten Online-APIs!** ⚡

---

## 🐛 Troubleshooting

### "llama-cli nicht gefunden"
→ Passe `LLAMA_CLI` Pfad in `config.py` an

### "Modell nicht gefunden"
→ Passe `MODEL_PATH` in `config.py` an

### "Vision funktioniert nicht"
→ Prüfe ob `MMPROJ_PATH` existiert

### Node erscheint nicht in ComfyUI
→ ComfyUI Console checken (Fehlerme


ldungen)
→ `python config.py` ausführen (zeigt Pfad-Fehler)

---

## 📝 Credits

- **Modell**: Qwen3-VL-30B von Alibaba (abliterated by tvall43)
- **Engine**: llama.cpp by ggerganov
- **Node**: Martin + Claude Coach (2026-02-13)

---

## 📜 Lizenz

MIT License - Nutze es wie du willst!

**Hinweis**: Das Modell selbst hat eigene Lizenzen (check HuggingFace)

---

## 🔗 Links

- [Qwen3-VL Modell](https://huggingface.co/tvall43/Huihui-Qwen3-VL-30B-A3B-Instruct-abliterated-Q4_K_M-GGUF)
- [llama.cpp](https://github.com/ggerganov/llama.cpp)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

---

**Viel Spaß mit zensurfreier Prompt-Generierung! 🔓🚀**
