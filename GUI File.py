from tkinter import Tk, Button, Label, Entry, LEFT, RIGHT

def createGUI():
    global rootWindow
    global canvas



    rootWindow = Tk()
    rootWindow.title("Run Tool")
    canvasAndGUI = Frame(rootWindow)
    canvas = Canvas(canvasAndGUI, height=200, width=200, relief=SUNKEN, borderwidth=2)
    canvas.pack(side=LEFT)
    rootWindow.mainloop()