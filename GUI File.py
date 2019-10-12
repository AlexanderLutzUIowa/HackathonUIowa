from tkinter import *

def createGUI():
    global rootWindow



    rootWindow = Tk()
    rootWindow.title("News Frequency Tool")
    topFrame = Frame(rootWindow)
    rootWindow.geometry('500x200')
    topFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    topFrame.columnconfigure(0, weight=1)
    topFrame.rowconfigure(0, weight=1)
    topFrame.pack(pady=100, padx=100)


    tkvariableMonth = StringVar(rootWindow)

    choices = {'January', 'February', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December'}
    tkvariableMonth.set('Month')  # set the default option

    popupMenu = OptionMenu(topFrame, tkvariableMonth, *choices)
    Label(mainframe, text="Choose a dish").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    # on change dropdown value
    def change_dropdown(*args):
        print(tkvar.get())

    instructionsLabel = Label(rootWindow, text = "This tool will pull data from the NY Times archive database"
                                                 " and find which word was most \n"
                                                 "frequent in the titles for that given month")
    instructionsLabel.pack()





    rootWindow.geometry('500x200')

    rootWindow.mainloop()

createGUI()