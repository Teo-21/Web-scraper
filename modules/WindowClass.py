from tkinter import *
from tkinter import ttk
import tkinter as tk
from modules.DataClass import *
from modules.DriverClass import *


class Window(Data,Driver):

    windowTitle : str
    windowIcon : str
    windowWidth : int
    windowHeight : int
    windowTk : object
    tabs : object
    tabMain : object
    tabAbout : object
    bgColor : str
    buttonsColor : str
    frameColor : str

    
    def __init__(self,bg="#931A25",btnColor="#F5EFEF",frameColor="#FFCB8E",windowInit= Tk()):

        self.windowTitle = "WEB SCRAPER v0.8.0"
        self.windowIcon = "icons/web_icon.ico"
        self.windowTk = windowInit
        self.windowWidth = 760
        self.windowHeight = 380
        self.tabs = ttk.Notebook(self.windowTk)
        self.bgColor = bg
        self.buttonsColor = btnColor
        self.frameColor = frameColor
        self.tabMain = Frame(self.tabs,bg= self.bgColor)
        self.tabAbout = Frame(self.tabs,bg= self.bgColor)
        # Driver.__init__(self)

    def centerProgramWindow(self):

        screenWidth = self.windowTk.winfo_screenwidth()
        screenHeight = self.windowTk.winfo_screenheight()
        x = (screenWidth // 2) - (self.windowWidth // 2)   
        y = (screenHeight // 2) - (self.windowHeight // 2)

        self.windowTk.geometry(f"{self.windowWidth}x{self.windowHeight}+{x}+{y}")

    def createTabs(self):

        self.tabs.add(self.tabMain,text='Main') 
        self.tabs.add(self.tabAbout,text='About')
        self.tabs.pack(expand=1, fill='both')

    def mainTabElements(self):

    # Creating label for main tab
    
        mainTabLabel = Label(self.tabMain,text="WEB SCRAPER v0.8.0",font=("Arial",18),bg=self.bgColor,fg=self.buttonsColor)
        mainTabLabel.grid(row=0,column=0,padx=(15,0),pady=(15,15))
        

    # Creating frame number one
        
        mainFrameOne = Frame(self.tabMain,width=210,height=230,bg=self.frameColor)
        mainFrameOne.grid(row=1,column=0,pady=(0,30))
        mainFrameOne.grid_propagate(FALSE)

    # Creating an image for frame number one

        scraperImg = PhotoImage(file="icons/scraper_image.pgm")
        imgLabel1 = Label(mainFrameOne,image=scraperImg)
        imgLabel1.image = scraperImg
        imgLabel1.grid(column=1,row=2,padx=(30,30),pady=(20,10))

    # Creating a button for frame number one
        
        scrapeData = Button(mainFrameOne,width=15,text="Scrape data",font=("Arial",10),bg=self.buttonsColor,command= lambda: self.scrapeData())
        scrapeData.grid(column=1,row=3)

    # Creating frame number two
        
        mainFrameTwo = Frame(self.tabMain,width=210,height=230,bg=self.frameColor)
        mainFrameTwo.grid(row=1,column=1,pady=(0,30))
        mainFrameTwo.grid_propagate(FALSE)

    # Creating an image for frame number two

        csvImg = PhotoImage(file="icons/csv_file.pgm")
        imgLabel2 = Label(mainFrameTwo,image=csvImg)
        imgLabel2.image = csvImg
        imgLabel2.grid(column=1,row=2,padx=(30,30),pady=(20,10)) 
        

    # Creating a button for frame number two    

        csvOption = Button(mainFrameTwo,width=15,text="Create CSV file",font=("Arial",10),bg=self.buttonsColor)
        csvOption.grid(column=1,row=3)

    # Creating frame number three

        mainFrameThree = Frame(self.tabMain,width=210,height=230,bg=self.frameColor)
        mainFrameThree.grid(row=1,column=2,pady=(0,30),padx=(30,40))
        mainFrameThree.grid_propagate(FALSE)

    # Creating an image for frame number three

        databaseImg = PhotoImage(file="icons/database.pgm")
        imgLabel3 = Label(mainFrameThree,image=databaseImg)
        imgLabel3.image = databaseImg
        imgLabel3.grid(column=1,row=2,padx=(30,30),pady=(20,10)) 
        

    # Creating a button for frame number three    

        databaseOption = Button(mainFrameThree,width=15,text="Store in database",font=("Arial",10),bg=self.buttonsColor)
        databaseOption.grid(column=1,row=3)

    # Copy right label creation    

        copyRight = Label(self.tabMain,text="© 2023 Teo-21",bg=self.bgColor,font=("Arial",12),fg=self.buttonsColor)
        copyRight.grid(column=1,row=3)

    # Exit program button creation

        exitButton = Button(self.tabMain,text="Exit program", command=self.windowTk.quit,bg=self.buttonsColor,width=15,font=("Arial",10))
        exitButton.grid(column=2,row=3,pady=(0,10),padx=(95,0))


    def aboutTabElements(self):
        # aboutTabLabel = Label(self.tabAbout,text="About WEB SCRAPER Software",bg=self.bgColor,font=("Arial",18))
        # aboutTabLabel.grid(column=0,row=0,padx=(15,0),pady=(15,15))    

        aboutTabText = Text(self.tabAbout,bg=self.buttonsColor,font=("Arial",11),width=71,height=22,padx=15,pady=5)
        text = self.readFromREADME()
        # text = "To be continued...I need to research how to strip markdown file so I can have plain text to display in here..."
        aboutTabText.insert(tk.END, text)
        aboutTabText.config(state=DISABLED)
        aboutTabText.grid(column=0,row=0,padx=(25,25))   

    