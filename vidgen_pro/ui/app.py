
import streamlit as st
import asyncio
import os
from vidgen_pro.utils.config import Config
from vidgen_pro.core.analyzer import ScriptAnalyzer
from vidgen_pro.core.visuals import VisualFetcher
from vidgen_pro.core.voice import VoiceGenerator
from vidgen_pro.editor.builder import VideoBuilder

# Ensure directories exist
Config.setup_dirs()

st.set_page_config(page_title="VidGen-Pro", page_icon="🎬", layout="wide")

st.title("🎬 VidGen-Pro: Production AI Video Editor")
st.markdown("### Turn your scripts into professional videos instantly.")

# Sidebar Configuration
st.sidebar.header("⚙️ Configuration")
api_key_google = st.sidebar.text_input("Google Gemini API Key", value=Config.GOOGLE_API_KEY or "", type="password")
api_key_pexels = st.sidebar.text_input("Pexels API Key", value=Config.PEXELS_API_KEY or "", type="password")

if api_key_google:
    Config.GOOGLE_API_KEY = api_key_google
    # Re-initialize analyzer with new key if provided
    # (In a real app, we might want a singleton or state management)

if api_key_pexels:
    Config.PEXELS_API_KEY = api_key_pexels

# Main UI
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. Script")
    script_text = st.text_area("Enter your video script here:", height=300, placeholder="In the heart of the city, a revolution was brewing...")
    
    voice_option = st.selectbox("Select Voice", ["en-US-ChristopherNeural", "en-US-JennyNeural", "en-US-GuyNeural"])
    
    generate_btn = st.button("🚀 Generate Video", type="primary")

with col2:
    st.subheader("2. Preview & Output")
    status_container = st.empty()
    video_container = st.empty()

async def run_generation(script, voice):
    status_container.info("🧠 Analyzing script...")
    analyzer = ScriptAnalyzer()
    scenes = analyzer.analyze_script(script)
    status_container.success(f"✅ Analyzed {len(scenes)} scenes.")
    
    # Visual Fetching
    status_container.info("🎥 Fetching stock footage...")
    fetcher = VisualFetcher()
    for scene in scenes:
        scene['visual_url'] = fetcher.fetch_video(scene['visual_query'])
    
    # Voiceover Generation
    status_container.info("🎙️ Generating voiceovers...")
    voice_gen = VoiceGenerator(voice=voice)
    audio_paths = []
    for i, scene in enumerate(scenes):
        filename = f"voice_{i}.mp3"
        path = await voice_gen.generate_voiceover(scene['text'], filename)
        audio_paths.append(path)

    # Thumbnail Generation
    status_container.info("🖼️ Generating thumbnail...")
    from vidgen_pro.core.thumbnail import ThumbnailGenerator
    thumb_gen = ThumbnailGenerator()
    thumbnail_path = thumb_gen.generate_thumbnail(script[:30] + "...", "AI Generated Video")
    
    # Video Assembly
    status_container.info("🎬 Assembling video (this may take a minute)...")
    builder = VideoBuilder()
    
    # Download visuals first (Builder can handle it, but let's be explicit or let builder do it)
    builder.retrieve_visuals(scenes)
    
    output_path = builder.assemble_video(scenes, audio_paths, output_filename="output_video.mp4")
    
    if output_path and os.path.exists(output_path):
        status_container.success("✨ Video Generated Successfully!")
        video_container.video(output_path)
        if thumbnail_path:
            st.image(thumbnail_path, caption="Generated Thumbnail")
    else:
        status_container.error("❌ Video generation failed.")

if generate_btn and script_text:
    if not Config.GOOGLE_API_KEY or not Config.PEXELS_API_KEY:
        st.warning("⚠️ Please provide API Keys in the sidebar to proceed.")
    else:
        # Run async loop
        asyncio.run(run_generation(script_text, voice_option))

