# VidGen-Pro: AI Video Editor

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-Apache%202.0-blue)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)

**VidGen-Pro** is a production-grade, fully automated AI video editing suite. It transforms raw text scripts into professional-quality videos complete with stock footage, realistic AI voiceovers, background music, and subtitles.

## 🚀 Features

- **Automated Script Analysis**: Uses Google Gemini Pro to identify scenes, moods, and visual keywords.
- **Smart Visual Fetching**: Integrates with Pexels API to find the perfect stock footage for each scene.
- **Realistic Voiceovers**: Powered by Edge-TTS for high-quality, natural-sounding narration.
- **Dynamic Video Assembly**: Automatically cuts, zooms, and assembles clips with transitions and overlays.
- **Subtitle Generation**: Whisper-based (or synchronized text) subtitles for accessibility and engagement.
- **Background Music**: Context-aware music selection (integration ready).

## 🛠️ Installation

```bash
pip install vidgen-pro
```

## 🚦 Usage

1. **Set API Keys**:
   Create a `.env` file in your project root:

   ```env
   PEXELS_API_KEY=your_pexels_key
   GOOGLE_API_KEY=your_gemini_key
   ```

2. **Run the Dashboard**:

   ```bash
   vidgen-pro
   ```

   Or explicitly via Streamlit:

   ```bash
   streamlit run vidgen_pro/ui/app.py
   ```

## 📦 Building from Source

```bash
git clone https://github.com/Shivay00001/vidgen-pro.git
cd vidgen-pro
pip install -e .
```

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---
**Author**: Shivay00001
