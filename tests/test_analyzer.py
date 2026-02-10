
import unittest
from vidgen_pro.core.analyzer import ScriptAnalyzer
from vidgen_pro.utils.config import Config

class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        # We can mock the API key to force the analyzer to init (even if it warns)
        # or we test the mock fallback if key is missing
        self.analyzer = ScriptAnalyzer()

    def test_mock_analysis(self):
        # If API key is missing, it should use mock analysis
        script = "This is a test script. It has two sentences."
        if not Config.GOOGLE_API_KEY:
            scenes = self.analyzer.analyze_script(script)
            self.assertEqual(len(scenes), 2)
            self.assertEqual(scenes[0]['text'], "This is a test script.")
            self.assertEqual(scenes[1]['text'], "It has two sentences.")
        else:
            print("Skipping mock test as API key is present.")

if __name__ == '__main__':
    unittest.main()
