from modules.WindowClass import *
from modules.DriverClass import *
from tkinter import ttk

def main():

# Creating program window

    w = Window()
    programWindow = w.windowTk
    programWindow.title(w.windowTitle)
    programWindow.iconbitmap(w.windowIcon)
    programWindow.geometry("800x600")

# Creating Tabs

    tabs = ttk.Notebook(programWindow)
    tabMain = ttk.Frame(tabs)
    tabSettings = ttk.Frame(tabs)
    tabAbout = ttk.Frame(tabs)
    tabs.add(tabMain,text='Main')
    tabs.add(tabSettings,text='Settings')
    tabs.add(tabAbout,text='About')
    tabs.pack(expand=1, fill='both')

# Tabs content

    ttk.Label(tabMain,text="Web scraper version 0.3.0").grid(column=0,row=0,padx=30,pady=30)
    ttk.Label(tabSettings,text="Basic settings").grid(column=0,row=0,padx=30,pady=30)
    ttk.Label(tabAbout,text="Info about this app will be added soon into this tab!").grid(column=0,row=0,padx=30,pady=30)
   
    programWindow.mainloop()
    

if __name__ == "__main__":
    main() 