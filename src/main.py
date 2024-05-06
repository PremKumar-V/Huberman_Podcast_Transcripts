from LinkScarper import Scarper
from DataExtracter import Extracter

scarper = Scarper()
extracter = Extracter()

if __name__ == "__main__":

    data = scarper.main()
    extracter.main(data)