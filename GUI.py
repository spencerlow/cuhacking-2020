import tkinter as tk


# window = TK()
# window.title("test")

window = tk.Tk()
window.geometry("700x250")
window.title("Murder mystery")
window.resizable(False, False)
window.configure(background="light grey")

def displayData():
    text = "test text here"
    dataWindow = tk.Tk()
    dataWindow.title("Data window")
    dataWindow.geometry("500x400")
    dataWindow.resizable(False, False)
    dataWindow.configure(background="light grey")

    #scrollbar
    # vertBar = tk.Scrollbar(dataWindow)
    # vertBar.pack(side="right", fill="y")

    #textbox
    # textBox = tk.Text(dataWindow, height = 10, width = 10)
    # textBox.grid(row=0,column=0)

    #entry widget


    textToutput = tk.Label(dataWindow, text = "Time", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "flat")
    textToutput.grid(row=0,column=1)

    textToutput = tk.Label(dataWindow, text = "Device", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "raised")
    textToutput.grid(row=0,column=2)

    textToutput = tk.Label(dataWindow, text = "Device ID", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "sunken")
    textToutput.grid(row=0,column=3)

    textToutput = tk.Label(dataWindow, text = "Event", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "ridge")
    textToutput.grid(row=0,column=4)

    textToutput = tk.Label(dataWindow, text = "Guest ID", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "solid")
    textToutput.grid(row=0,column=5)

    textToutput = tk.Label(dataWindow, text = "EXTRA", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "groove")
    textToutput.grid(row=0,column=6)

    sampleGrid = tk.Label(dataWindow,text = "-------",borderwidth = 1, relief = "groove")
    for r in range(1,10):
        for c in range(1,7):
            sampleGrid = tk.Label(dataWindow,text = "-------",borderwidth = 1, relief = "groove")
            sampleGrid.grid(row=r,column=c)


#Groups

##hotel guests
###Veronica, Jason, Thomas, Rob, Kristina
textoutput = tk.Label(window, text = "Hotel guests", bg="dark grey" ,fg="black", font=("Felix Titling",16,"bold"))
textoutput.place(x=100,y=20)

testButton = tk.Button(text = "Veronica", command = displayData)
testButton.place(x=100,y=60)
testButton = tk.Button(text = "Jason", command = displayData)
testButton.place(x=100,y=100)
testButton = tk.Button(text = "Thomas", command = displayData)
testButton.place(x=100,y=140)
testButton = tk.Button(text = "Kristina", command = displayData)
testButton.place(x=100,y=180)


##hotel staff
###Marc-Andre,Dave,Salina,Harrison
textoutput = tk.Label(window, text = "Hotel staff", bg="dark grey" ,fg="black", font=("Felix Titling",16,"bold"))
textoutput.place(x=300,y=20)

testButton = tk.Button(text = "Marc-Andre", command = displayData)
testButton.place(x=300,y=60)
testButton = tk.Button(text = "Dave", command = displayData)
testButton.place(x=300,y=100)
testButton = tk.Button(text = "Salina", command = displayData)
testButton.place(x=300,y=140)
testButton = tk.Button(text = "Harrison", command = displayData)
testButton.place(x=300,y=180)

##random people
###eugune???
textoutput = tk.Label(window, text = "Unidentified", bg="dark grey" ,fg="black", font=("Felix Titling",16,"bold"))
textoutput.place(x=480,y=20)

testButton = tk.Button(text = "Eugene", command = displayData)
testButton.place(x=480,y=60)
testButton = tk.Button(text = "Alok", command = displayData)
testButton.place(x=480,y=100)



userEntry = tk.Entry(window)
userEntry.place(x=500,y=200)


def searchClick():
    #SEARCH ENTRY STORES THE USER INPUT<--------------------------------------------------
    searchEntry = userEntry.get()
    print(searchEntry)
    searchWindow = tk.Tk()
    searchWindow.title("Search Window")
    searchWindow.geometry("500x400")
    searchWindow.resizable(False, False)
    searchWindow.configure(background="#DA806C")
    # tk.Text

#a button that uses the function above
tk.Button(window,text="SEARCH",command=searchClick).place(x=445,y=200)


# new comment additional line

window.mainloop()

# if __name__ == "__main__":
#     window.mainloop()
