import os.path
from markdown import Markdown
from io import StringIO

# markdown and io imports are for markdown file stripping, which will be done soon hopefully

class Data:

    fileData : str


    def __init__(self):
        pass

    def readFromREADME(self):

        readmeFile = open("README.md","r")
        self.fileData = readmeFile.read()
        readmeFile.close()
        return self.fileData

