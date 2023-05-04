from tkinter import *
from tkinter import ttk

class Window:

    windowTitle : str
    windowIcon : str
    windowResX : int
    windowResY : int
    windowTk : object
    bgColor : str
    
    def __init__(self):

        self.windowTitle = "Web scraper"
        self.windowIcon = "icons/web_icon.ico"
        self.windowResX = 800
        self.windowResY = 600
        self.windowTk = Tk()
        self.bgColor = "#FEFF86"
    
   