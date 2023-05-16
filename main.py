from modules.WindowClass import *


def main():

# Window initialization and theme changing functionality

    w = Window()
    programWindow = w.windowTk
    programWindow.title(w.windowTitle)
    programWindow.iconbitmap(w.windowIcon)
    w.centerProgramWindow()
    dropdownOption = StringVar()
    options = [

        "Default",
        "Midnight blue & Daisy bush",
        "Alice blue & Rock blue",
        "Laurel & Norway"
    ]
   # Default window theme initialization

    dropdownOption.set(options[1])
    bg,btn,frame = Window.changeTheme(dropdownOption.get())
    print(bg,btn,frame)

    
    themeChanger = Window(bg,btn,frame)
        
# Calling a method for tab creation

    themeChanger.createTabs()
    
# Calling a method for main tab layout creation

    themeChanger.mainTabElements()

# Calling a method for settings tab layout creation

    themeChanger.settingsTabElements(dropdownOption,options)

    programWindow.mainloop()
    

if __name__ == "__main__":
    main() 