from tkinter import *
from tkinter import ttk


class Window:

    windowTitle : str
    windowIcon : str
    windowWidth : int
    windowHeight : int
    windowTk : object
    tabs : object
    tabMain : object
    tabSettings : object
    tabAbout : object
    bgColor : str
    buttonsColor : str
    
    def __init__(self):

        self.windowTitle = "WEB SCRAPER v0.6.0"
        self.windowIcon = "icons/web_icon.ico"
        self.windowTk = Tk()
        self.windowWidth = 760
        self.windowHeight = 380
        self.tabs = ttk.Notebook(self.windowTk)
        self.bgColor = "#B0DAFF"
        self.buttonsColor = "#FEFF86"
        self.tabMain = Frame(self.tabs,bg= self.bgColor)
        self.tabSettings = Frame(self.tabs,bg= self.bgColor)
        self.tabAbout = Frame(self.tabs,bg= self.bgColor)

    def centerProgramWindow(self):

        screenWidth = self.windowTk.winfo_screenwidth()
        screenHeight = self.windowTk.winfo_screenheight()
        x = (screenWidth // 2) - (self.windowWidth // 2)   
        y = (screenHeight // 2) - (self.windowHeight // 2)

        self.windowTk.geometry(f"{self.windowWidth}x{self.windowHeight}+{x}+{y}")

    def createTabs(self):

        self.tabs.add(self.tabMain,text='Main') 
        self.tabs.add(self.tabSettings,text='Settings')
        self.tabs.add(self.tabAbout,text='About')
        self.tabs.pack(expand=1, fill='both')

    def mainTabElements(self):

    # Creating label for main tab
    
        mainTabLabel = Label(self.tabMain,text="WEB SCRAPER v0.6.0",font=("Arial",18),bg=self.bgColor)
        mainTabLabel.grid(row=0,column=0,padx=(15,0),pady=(15,15))
        

    # Creating frame number one
        
        mainFrameOne = Frame(self.tabMain,width=210,height=230,bg="#19A7CE")
        mainFrameOne.grid(row=1,column=0,pady=(0,30))
        mainFrameOne.grid_propagate(FALSE)

    # Creating an image for frame number one

        scraperImg = PhotoImage(file="icons/scraper_image.pgm")
        imgLabel1 = Label(mainFrameOne,image=scraperImg)
        imgLabel1.image = scraperImg
        imgLabel1.grid(column=1,row=2,padx=(30,30),pady=(20,10))

    # Creating a button for frame number one
        
        scrapeData = Button(mainFrameOne,width=15,text="Scrape data",font=("Arial",10),bg=self.buttonsColor,cursor="spider")
        scrapeData.grid(column=1,row=3)

    # Creating frame number two
        
        mainFrameTwo = Frame(self.tabMain,width=210,height=230,bg="#19A7CE")
        mainFrameTwo.grid(row=1,column=1,pady=(0,30))
        mainFrameTwo.grid_propagate(FALSE)

    # Creating an image for frame number two

        csvImg = PhotoImage(file="icons/csv_file.pgm")
        imgLabel2 = Label(mainFrameTwo,image=csvImg)
        imgLabel2.image = csvImg
        imgLabel2.grid(column=1,row=2,padx=(30,30),pady=(20,10)) 
        

    # Creating a button for frame number two    

        csvOption = Button(mainFrameTwo,width=15,text="Create CSV file",font=("Arial",10),bg=self.buttonsColor,cursor="spider")
        csvOption.grid(column=1,row=3)

    # Creating frame number three

        mainFrameThree = Frame(self.tabMain,width=210,height=230,bg="#19A7CE")
        mainFrameThree.grid(row=1,column=2,pady=(0,30),padx=(30,40))
        mainFrameThree.grid_propagate(FALSE)

    # Creating an image for frame number three

        databaseImg = PhotoImage(file="icons/database.pgm")
        imgLabel3 = Label(mainFrameThree,image=databaseImg)
        imgLabel3.image = databaseImg
        imgLabel3.grid(column=1,row=2,padx=(30,30),pady=(20,10)) 
        

    # Creating a button for frame number three    

        databaseOption = Button(mainFrameThree,width=15,text="Store in database",font=("Arial",10),bg=self.buttonsColor,cursor="spider")
        databaseOption.grid(column=1,row=3)

    # Copy right label creation    

        copyRight = Label(self.tabMain,text="© 2023 Teo-21",bg=self.bgColor,font=("Arial",12))
        copyRight.grid(column=1,row=3)

    # Exit program button creation

        exitButton = Button(self.tabMain,text="Exit program", command=self.windowTk.quit,bg=self.buttonsColor,width=15,font=("Arial",10))
        exitButton.grid(column=2,row=3,pady=(0,10),padx=(95,0))

    def settingsTabElements(self):

    # Label for settings tab

        settingsLabel = Label(self.tabSettings,text="Settings",font=("Arial",18),bg=self.bgColor) 
        settingsLabel.grid(row=0,column=0,padx=(15,0),pady=(15,15))

    # Label for theme change option
        
        themeOption = Label(self.tabSettings,text="Theme",font=("Arial",12),bg=self.bgColor)
        themeOption.grid(row=1,column=0)

    # dropdown menu for theme selection

        dropdownOption = StringVar()
        options = [

            "Default",
            "Midnight blue & Daisy bush",
            "Alice blue & Rock blue",
            "Laurel & Norway"
        ]
        dropdownOption.set(options[0])
        themeDropdown = OptionMenu(self.tabSettings,dropdownOption, *options) 
        themeDropdown.grid(column=1,row=1,padx=(15,0))   