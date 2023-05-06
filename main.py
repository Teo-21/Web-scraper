from modules.WindowClass import *
from modules.DriverClass import *



def main():

# Creating program window

    w = Window()
    programWindow = w.windowTk
    programWindow.title(w.windowTitle)
    programWindow.iconbitmap(w.windowIcon)
    programWindow.geometry(w.windowGeometry)

# Creating Tabs

    w.createTabs()
    
# Main tab layout

    w.mainTabElements()

    programWindow.mainloop()
    

if __name__ == "__main__":
    main() 