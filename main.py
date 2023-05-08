from modules.WindowClass import *
from modules.DriverClass import *



def main():

# Creating program window

    w = Window()
    programWindow = w.windowTk
    programWindow.title(w.windowTitle)
    programWindow.iconbitmap(w.windowIcon)
    w.centerProgramWindow()
    
# Calling a method for tab creation

    w.createTabs()
    
# Calling a method for main tab layout creation

    w.mainTabElements()

    programWindow.mainloop()
    

if __name__ == "__main__":
    main() 