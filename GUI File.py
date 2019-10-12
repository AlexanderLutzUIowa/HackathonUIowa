from tkinter import Tk, Canvas, Frame, Button, Label, Entry, END, LEFT, RIGHT, SUNKEN

def createGUI():
    global rootWindow
    global canvas



    rootWindow = Tk()
    rootWindow.title("Run Tool")
    canvasAndGUI = Frame(rootWindow)
    canvas = Canvas(canvasAndGUI, height=200, width=200, relief=SUNKEN, borderwidth=2)
    canvas.pack(side=LEFT)

    guiFrame = Frame(canvasAndGUI)

    ballsFrame = Frame(guiFrame)
    takeLabel = Label(ballsFrame, text='Take')
    numBallsEntry = Entry(ballsFrame)
    ballsLabel = Label(ballsFrame, text='balls')
    takeLabel.pack(side=LEFT)
    numBallsEntry.pack(side=LEFT)
    ballsLabel.pack()

    heapFrame = Frame(guiFrame)
    heapLabel = Label(heapFrame, text='from heap')
    whichHeapEntry = Entry(heapFrame)
    heapLabel.pack(side=LEFT)
    whichHeapEntry.pack()







    rootWindow.mainloop()