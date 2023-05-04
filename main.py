from modules.WindowClass import *


def main():

    w = Window()
    programWindow = w.windowTk
    programWindow.title(w.windowTitle)
    programWindow.iconbitmap(w.windowIcon)
    programWindow.configure(width= w.windowResX, height = w.windowResY)
    programWindow.configure(bg= w.bgColor)
    programWindow.mainloop()
    

if __name__ == "__main__":
    main()