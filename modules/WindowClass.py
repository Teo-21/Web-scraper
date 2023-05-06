from tkinter import *
from tkinter import ttk

class Window:

    windowTitle : str
    windowIcon : str
    windowGeometry : str
    windowTk : object
    tabs : object
    tabMain : object
    tabSettings : object
    tabAbout : object
    bgColorOne : str
    
    def __init__(self):

        self.windowTitle = "Web scraper"
        self.windowIcon = "icons/web_icon.ico"
        self.windowTk = Tk()
        self.windowGeometry = "800x600"
        self.tabs = ttk.Notebook(self.windowTk)
        self.bgColorOne = "#B0DAFF"
        self.tabMain = Frame(self.tabs,bg= self.bgColorOne)
        self.tabSettings = Frame(self.tabs,bg= self.bgColorOne)
        self.tabAbout = Frame(self.tabs,bg= self.bgColorOne)
       

    def createTabs(self):

        self.tabMain
        self.tabSettings
        self.tabAbout
        self.tabs.add(self.tabMain,text='Main') 
        self.tabs.add(self.tabSettings,text='Settings')
        self.tabs.add(self.tabAbout,text='About')
        self.tabs.pack(expand=1, fill='both')

    def mainTabElements(self):
        
        mainFrameOne = Frame(self.tabMain,width=250,height=280,bg="#19A7CE")
        mainFrameOne.pack(side=LEFT,padx=10)
        mainFrameTwo = Frame(self.tabMain,width=250,height=280,bg="#19A7CE")
        mainFrameTwo.pack(side=LEFT,padx=10)
        mainFrameThree = Frame(self.tabMain,width=250,height=280,bg="#19A7CE")
        mainFrameThree.pack(side=LEFT,padx=10)