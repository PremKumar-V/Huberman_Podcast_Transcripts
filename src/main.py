from Scraper.LinkScarper import Scarper
from Scraper.DataExtracter import Extracter

from Updater import updater

scarper = Scarper()
extracter = Extracter()

if __name__ == "__main__":

    data = scarper.main()
    extracter.main(data)
    updater()
