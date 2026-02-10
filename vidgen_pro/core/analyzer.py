
import google.generativeai as genai
import json
import logging
from vidgen_pro.utils.config import Config

logger = logging.getLogger(__name__)

class ScriptAnalyzer:
    def __init__(self):
        if Config.GOOGLE_API_KEY:
            genai.configure(api_key=Config.GOOGLE_API_KEY)
            self.model = genai.GenerativeModel('gemini-pro')
        else:
            self.model = None
            logger.warning("Google API Key not found. Analysis capabilities will be limited or mocked.")

    def analyze_script(self, script_text):
        """
        Analyzes the script and breaks it down into scenes with visual search queries.
        """
        if not self.model:
            return self._mock_analysis(script_text)

        prompt = f"""
        You are an expert video editor and director. 
        Analyze the following script and break it down into scenes. 
        For each scene, provide:
        1. "text": The exact segment of the script.
        2. "visual_query": A short, effective search query for stock footage (e.g., "futuristic city drone shot", "happy diverse team meeting").
        3. "mood": The mood of the scene (e.g., "inspiring", "tense", "calm").
        4. "duration_est": Estimated duration in seconds (rough guess based on text length).
        
        Return the result as a strictly valid JSON list of objects. Do not include markdown code block syntax.

        Script:
        {script_text}
        """

        try:
            response = self.model.generate_content(prompt)
            # Cleanup potential markdown formatting if the model adds it
            clean_text = response.text.replace('```json', '').replace('```', '').strip()
            scenes = json.loads(clean_text)
            return scenes
        except Exception as e:
            logger.error(f"Error analyzing script: {e}")
            return self._mock_analysis(script_text)

    def _mock_analysis(self, script_text):
        """Fallback if API fails or is missing"""
        # Split by newlines or periods roughly
        segments = [s.strip() for s in script_text.split('.') if s.strip()]
        scenes = []
        for i, segment in enumerate(segments):
            scenes.append({
                "text": segment + ".",
                "visual_query": "cinematic generic footage",
                "mood": "neutral",
                "duration_est": len(segment) / 15  # Rough approx
            })
        return scenes
