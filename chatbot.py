from google import genai
from google.genai import types

from config import Config
from prompts import SYSTEM_PROMPT


class AICareerMentor:
    """
    AI Career Mentor chatbot powered by Google's Gemini API.
    """

    def __init__(self):
        self.client = genai.Client(api_key=Config.GEMINI_API_KEY)

    def chat(self, user_message: str) -> str:
        """
        Sends a user message to Gemini along with the system prompt
        and returns the generated response.
        """

        try:
            response = self.client.models.generate_content(
                model=Config.MODEL_NAME,
                contents=user_message,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    temperature=Config.TEMPERATURE,
                    max_output_tokens=Config.MAX_OUTPUT_TOKENS,
                ),
            )

            return response.text

        except Exception as error:
            return f"An error occurred: {error}"