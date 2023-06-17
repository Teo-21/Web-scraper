from modules.WindowClass import *



def main():

# Window initialization and theme changing functionality

    w = Window()
    programWindow = w.windowTk
    programWindow.title(w.windowTitle)
    programWindow.iconbitmap(w.windowIcon)
    w.centerProgramWindow()   
    w.createTabs()
    
# Calling a method for main tab layout creation

    w.mainTabElements()


# calling a method for about tab creation

    w.aboutTabElements()

# window main loop 

    programWindow.mainloop()
    

if __name__ == "__main__":
    main() 