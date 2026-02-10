
import asyncio
import edge_tts
import os
from vidgen_pro.utils.config import Config
import logging

logger = logging.getLogger(__name__)

class VoiceGenerator:
    def __init__(self, voice="en-US-ChristopherNeural"):
        self.voice = voice
        self.output_dir = os.path.join(Config.TEMP_DIR, "audio")
        os.makedirs(self.output_dir, exist_ok=True)

    async def generate_voiceover(self, text, filename):
        """
        Generates voiceover using Edge TTS.
        """
        output_path = os.path.join(self.output_dir, filename)
        
        try:
            communicate = edge_tts.Communicate(text, self.voice)
            await communicate.save(output_path)
            return output_path
        except Exception as e:
            logger.error(f"Error generating voiceover: {e}")
            return None

    def get_available_voices(self):
        # This could be expanded to list available voices dynamically
        return [
            "en-US-ChristopherNeural",
            "en-US-EricNeural",
            "en-US-GuyNeural",
            "en-US-JennyNeural",
            "en-US-MichelleNeural"
        ]
