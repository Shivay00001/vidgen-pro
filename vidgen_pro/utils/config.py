
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    OUTPUT_DIR = "output_videos"
    ASSETS_DIR = "assets"
    FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")
    TEMP_DIR = "temp"

    @staticmethod
    def validate_keys():
        missing = []
        if not Config.PEXELS_API_KEY:
            missing.append("PEXELS_API_KEY")
        if not Config.GOOGLE_API_KEY:
            missing.append("GOOGLE_API_KEY")
        return missing

    @staticmethod
    def setup_dirs():
        os.makedirs(Config.OUTPUT_DIR, exist_ok=True)
        os.makedirs(Config.ASSETS_DIR, exist_ok=True)
        os.makedirs(Config.FONTS_DIR, exist_ok=True)
        os.makedirs(Config.TEMP_DIR, exist_ok=True)
