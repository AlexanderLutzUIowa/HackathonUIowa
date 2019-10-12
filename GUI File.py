from tkinter import Tk, Canvas, Frame, Button, Label, Entry, END, LEFT, RIGHT, SUNKEN

def createGUI():
    global rootWindow



    rootWindow = Tk()
    rootWindow.title("News Frequency Tool")
    instructionsLabel = Label(rootWindow, text = "This tool will pull data from the NY Times archive database"
                                                 " and find which word was most \n"
                                                 "frequent in the titles for that given month")
    instructionsLabel.grid(column = 0, row = 0)



    rootWindow.geometry('500x200')

    rootWindow.mainloop()

createGUI()