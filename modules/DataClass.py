import markdown
from bs4 import BeautifulSoup


class Data:

    fileData : str


    def __init__(self):
        pass

    def readFromREADME(self):

        readmeFile = markdown.markdown(open("README.md").read())
        fileContent = BeautifulSoup(readmeFile,"html.parser")
        readmeContent = "".join(fileContent.findAll(text = True))
        return readmeContent


