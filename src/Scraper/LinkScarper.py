import requests
from bs4 import BeautifulSoup

from Scraper.MainScraper import ScarperClass
from typing import List


class Scarper(ScarperClass):
    def __init__(self) -> None:
        super().__init__()

    def extractResponse(self, response) -> List:
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            links = soup.find("div", class_="flex flex-col").find_all("a")
            linkArray = []
            for link in links:
                linkArray.append(f"{self.value.baseUrl}{link['href']}")
            return linkArray

        else:
            raise requests.exceptions.HTTPError(
                f"HTTP Error, Status Code: {response.status_code}"
            )

    def main(self):
        responseFromScraper = self.scrape(self.value.homePageUrl)
        return self.extractResponse(responseFromScraper)
