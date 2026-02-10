# 🔥 Ready-to-Build AI Video Editor (MrBeast, Dhruv Rathee, Iman Gadzhi style)

## 🧠 Core Features (All Automated)
1. **Script Input** (You paste text or upload voice)
2. **Script Analyzer** – Break into sections: Hook, Build, Climax, CTA
3. **Auto Visual Fetcher** – Searches royalty-free visuals (Pexels API)
4. **Voiceover Generator** – Clone realistic voices (via Bark or Tortoise TTS)
5. **Auto Music Sync** – Background music with dynamic shifts
6. **Video Assembly** – Auto-cut visuals + text overlays + b-roll + zoom
7. **Subtitle Generator** – Auto highlight key phrases
8. **Thumbnail Generator** – Generates viral thumbnail from prompt
9. **Export for YouTube + Shorts**

---

## 🧰 Free Tools Used
- **Python** + `moviepy`, `opencv-python`, `transformers`
- **Pexels API** (for video B-roll)
- **Bark / Tortoise TTS** (for voiceover)
- **Streamlit** (UI)
- **Remixicon / Emojipedia** (emoji overlays)
- **Freesound.org API** (background SFX)
- **HuggingFace Transformers** (for NLP analysis)
- **Stable Diffusion (via Replicate API)** – For thumbnail & image prompts
- **FFmpeg** – Final rendering backend

---

## 📁 Folder Structure
```
project_folder/
├── app.py                    # Streamlit app UI
├── editor/
│   ├── script_analyzer.py    # NLP-based section breaker
│   ├── visual_fetcher.py     # Pexels API fetch logic
│   ├── voiceover.py          # Text-to-speech (Bark or Tortoise)
│   ├── music_sync.py         # Music matcher
│   ├── video_builder.py      # MoviePy logic
│   ├── thumbnail_gen.py      # Stable Diffusion prompt to image
│   └── subtitle_gen.py       # Subtitle overlays
├── assets/
│   ├── music/                # Free background music
│   └── sfx/                  # SFX audio
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup Instructions
```bash
# Clone repo
$ git clone https://github.com/yourrepo/ai-video-editor
$ cd ai-video-editor

# Setup venv
$ python -m venv venv
$ source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
$ pip install -r requirements.txt

# Add Pexels API Key in .env file
PEXELS_API_KEY=your_key_here

# Run the app
$ streamlit run app.py
```

---

## 🧪 Bonus Add-ons (Optional)
- [ ] **Face Animation**: Use SadTalker to animate AI narrator
- [ ] **Lip Sync to Script**: Wav2Lip integration
- [ ] **Real-Time Trending Hooks**: GPT-4 scraping from Reddit/Twitter
- [ ] **YT SEO Integration**: Auto title/description/tags (YouTube API)

---

## 🔁 Future Versions
- Add **voice emotion detection**
- Add **hand gesture overlays** like Dhruv Rathee’s editor
- Auto **chapter detection** & **interactive content timeline**

---

## 🧠 Use Case Example
> "You paste your documentary script → choose style (MrBeast / Dhruv / Documentary / Saqlain Khan) → it fetches visuals + voice + edit → outputs full HD video ready for upload."

Ready to build. If you want this in Hindi or want a no-code version (like Glide or Bubble), I can convert it.
