
import requests
import os
import random
from vidgen_pro.utils.config import Config
import logging

logger = logging.getLogger(__name__)

class VisualFetcher:
    BASE_URL = "https://api.pexels.com/videos/search"
    
    def __init__(self):
        self.headers = {
            "Authorization": Config.PEXELS_API_KEY
        }
        if not Config.PEXELS_API_KEY:
            logger.warning("Pexels API Key missing. Visual fetching will fail.")

    def fetch_video(self, query, duration_min=5, orientation="landscape"):
        """
        Fetches a video URL from Pexels based on the query.
        """
        if not Config.PEXELS_API_KEY:
            return None

        params = {
            "query": query,
            "per_page": 5,
            "orientation": orientation,
            "size": "medium" # or large/hd
        }

        try:
            response = requests.get(self.BASE_URL, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            if not data.get('videos'):
                logger.info(f"No videos found for query: {query}")
                return None

            # Select a random video from the top results
            video = random.choice(data['videos'])
            
            # Get the best quality link that matches our needs (720p or 1080p usually)
            video_files = video.get('video_files', [])
            
            # Sort by width to get decent quality
            video_files.sort(key=lambda x: x['width'], reverse=True)
            
            # Return high quality link
            for vf in video_files:
                if vf['quality'] == 'hd' and vf['width'] >= 1280:
                    return vf['link']
            
            # Fallback
            return video_files[0]['link'] if video_files else None

        except Exception as e:
            logger.error(f"Error fetching visual from Pexels: {e}")
            return None

    def download_video(self, url, filename):
        """Downloads the video to the local assets folder."""
        if not url:
            return None
            
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            path = os.path.join(Config.TEMP_DIR, filename)
            with open(path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            return path
        except Exception as e:
            logger.error(f"Error downloading video: {e}")
            return None
