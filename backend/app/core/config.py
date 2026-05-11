import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    def __init__(self):

        self.GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

        self.MAX_CONTENT_LENGTH = 12000

settings = Settings()