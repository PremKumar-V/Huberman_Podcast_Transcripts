import requests
from utils import Values


class ScarperClass:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.value = Values()

    def scrape(self, link) -> requests.Response:
        try:
            response = self.session.get(url=link, headers=self.value.headers)
            return response
        except requests.RequestException as error:
            raise requests.exceptions.RequestException(f"Error in Requesting: {error}")
