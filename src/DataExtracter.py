import requests
from bs4 import BeautifulSoup


from MainScraper import ScarperClass


class Extracter(ScarperClass):
    def __init__(self) -> None:
        super().__init__()

    def extract(self, link) -> str:
        response = self.scrape(link)
        soup = BeautifulSoup(response.text, "html.parser")

        data = soup.find_all("p", class_="break-words whitespace-pre-wrap")
        for text in data:
            textContent = text.get_text(separator=" ", strip=True)
            with open(link.split('/')[-1] + '.txt', 'w') as file:
                file.writelines(textContent)

    def main(self, linkArray):
        for link in linkArray:
            self.extract(link)
            break
