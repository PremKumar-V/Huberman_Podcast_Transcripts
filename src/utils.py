import os
from dotenv import load_dotenv

class Values:
    def __init__(self) -> None:
        load_dotenv()
        self.baseUrl = os.getenv("BASEURL")
        self.homePageUrl = self.baseUrl + os.getenv("HOMEPAGE")
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        }
