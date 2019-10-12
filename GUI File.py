from tkinter import *

def createGUI():
    global rootWindow



    rootWindow = Tk()
    rootWindow.title("News Frequency Tool")

    entryFrame = Frame(rootWindow)
    rootWindow.geometry('1000x600')
    entryFrame.columnconfigure(0, weight=1)
    entryFrame.rowconfigure(2, weight=1)
    yearEntryBox = Entry(entryFrame)
    yearEntryBox.grid(row=0, column=2)


    tkvariableMonth = StringVar(rootWindow)

    choices = {'January', 'February', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December'}
    tkvariableMonth.set('Month')  # set the default option

    popupMenu = OptionMenu(entryFrame, tkvariableMonth, *choices)

    popupMenu.grid(row=0, column=1)










    titleFrame = Frame(rootWindow)
    titleFrame.columnconfigure(0, weight=1)
    titleFrame.rowconfigure(0, weight=1)


    instructionsLabel = Label(titleFrame, text="This tool will pull data from the NY Times archive database"
                                               " and find which word was most \n"
                                               "frequent in the titles for that given month")
    instructionsLabel.pack()






    entryTitleFrame = Frame(rootWindow)
    entryTitleFrame.columnconfigure(0, weight=1)
    entryTitleFrame.rowconfigure(1, weight=1)

    monthAndYearLabel = Label(entryTitleFrame, text="Choose a month and enter a year")

    monthAndYearLabel.pack()









    def buttonClicked():
        monthNum = None
        if (tkvariableMonth.get() == "Month"):
            print("Choose a valid month")

        elif (tkvariableMonth.get() == "January"):
            monthNum = 1

        elif (tkvariableMonth.get() == "February"):
            monthNum = 2

        elif (tkvariableMonth.get() == "March"):
            monthNum = 3

        elif (tkvariableMonth.get() == "April"):
            monthNum = 4

        elif (tkvariableMonth.get() == "May"):
            monthNum = 5

        elif (tkvariableMonth.get() == "June"):
            monthNum = 6

        elif (tkvariableMonth.get() == "July"):
            monthNum = 7

        elif (tkvariableMonth.get() == "August"):
            monthNum = 8

        elif (tkvariableMonth.get() == "September"):
            monthNum = 9

        elif (tkvariableMonth.get() == "October"):
            monthNum = 10

        elif (tkvariableMonth.get() == "November"):
            monthNum = 11

        elif (tkvariableMonth.get() == "December"):
            monthNum = 12


        print(monthNum)



        if (tkvariableMonth.get() != "Month" and yearEntryBox.get() != ""):
            print(yearEntryBox.get())

    buttonFrame = Frame(rootWindow)
    buttonFrame.columnconfigure(0, weight=1)
    buttonFrame.rowconfigure(3, weight=1)

    runToolButton = Button(buttonFrame, text="Run Tool", command=buttonClicked)
    runToolButton.pack()

    titleFrame.pack(pady=20, padx=10)
    entryTitleFrame.pack()
    entryFrame.pack(pady=10, padx=10)
    buttonFrame.pack(pady=10)


    rootWindow.mainloop()

createGUI()