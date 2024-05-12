import google.generativeai as genai
from dotenv import dotenv_values


class GoogleGemini:
    def __init__(self, model_name) -> None:
        self._configs = dotenv_values()
        genai.configure(api_key=self._configs["GOOGLE_API_KEY"])
        self._model = genai.GenerativeModel(
            model_name,
            safety_settings=self.get_safety_settings(),
            generation_config=self.get_generation_settings(),
        )

    def get_generation_settings(self):
        return {
            "candidate_count": 1,
            "temperature": 0.5,
        }

    def get_safety_settings(self):
        return {
            "HARASSMENT": "BLOCK_NONE",
            "HATE": "BLOCK_NONE",
            "SEXUAL": "BLOCK_NONE",
            "DANGEROUS": "BLOCK_NONE",
        }

    def generate_content(self, prompt):
        return self._model.generate_content(prompt)

    def start_chat(self, history=[]):
        return self._model.start_chat(history=history)
