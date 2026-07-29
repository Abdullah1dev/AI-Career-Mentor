import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    MODEL_NAME = "gemini-3.5-flash"

    MAX_OUTPUT_TOKENS = 512

    TEMPERATURE = 0.7