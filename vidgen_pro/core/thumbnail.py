
from PIL import Image, ImageDraw, ImageFont
import os
from vidgen_pro.utils.config import Config
import random

class ThumbnailGenerator:
    def __init__(self):
        self.output_dir = os.path.join(Config.TEMP_DIR, "thumbnails")
        os.makedirs(self.output_dir, exist_ok=True)
        # Try to load a font, fallback to default if not found
        try:
            self.font = ImageFont.truetype("arial.ttf", 60)
        except:
            self.font = ImageFont.load_default()

    def generate_thumbnail(self, title, subtitle=None, bg_color=None):
        """
        Generates a youtube-style thumbnail.
        """
        width, height = 1280, 720
        if not bg_color:
            # Random darkish color
            bg_color = (random.randint(0, 50), random.randint(0, 50), random.randint(50, 100))
        
        img = Image.new('RGB', (width, height), color=bg_color)
        draw = ImageDraw.Draw(img)

        # Draw Title
        # Centering text is a bit manual without newer PIL features or font metrics
        # Simple implementation
        
        # Draw some "modern" shapes for style
        draw.rectangle([(0, 0), (width, 100)], fill=(0,0,0))
        draw.rectangle([(0, height-100), (width, height)], fill=(0,0,0))

        # Title
        draw.text((50, 200), title, font=self.font, fill=(255, 255, 0)) # Yellow
        
        if subtitle:
            draw.text((50, 350), subtitle, font=self.font, fill=(255, 255, 255))

        filename = f"thumb_{hash(title)}.jpg"
        path = os.path.join(self.output_dir, filename)
        img.save(path)
        return path
