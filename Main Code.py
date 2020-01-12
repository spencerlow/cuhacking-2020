
read = open("Murder-on-the-2nd-Floor-Raw-Data.json", "r")
line = read.readline()
##This is used to store the time line with unwanted characters
rough = []

##Variables to temporarily store input get reset every 5 lines
time = " "
device = ""
device_id = ""
event = ""
guest = ""
##Lists of people names
names = {}
Individuals = []
Rob = []
Veronica = []
Jason = []
Thomas = []
Kristina = []
Marc_Andre = []
Dave = []
Salina = []
Harrison = []
Eugene = []
alok = []
na = []
unknown = []
master_list =[]

def timetoepoch():
    zeinput = input("Input time in format YYYY-MM-DD HH:MM:SS ")
    import calendar, time; return (calendar.timegm(time.strptime(zeinput, '%Y-%m-%d %H:%M:%S')))

def epochtotime(epokk):
    varb = epokk
    import time; return time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(int(varb)))

##Variables that are used to count as timers
line_count = 0

while line != "":
    if line_count == 0:
        line_count +=1
    else:
        if line_count == 1:
            #This line reads in the time stamp line and
            time = ""
            del rough[:]
            for a in line:
                rough.append(a)
            if len(rough) == 1:
                break
            for x in range (5,15):
                time += rough[x]
            time = time.strip("\"")
            time = time.strip()
            master_list.append(time)
            time = epochtotime(time)

            line_count +=1
        elif line_count == 2:
            ##Code to determine what type of access point was used
            if line.find("access") != -1:
                device = "access point"
            elif line.find("Door") != -1:
                device = "Door Sensor"
            elif line.find("motion") != -1:
                device = "motion sensor"
            elif line.find("phone") != -1:
                device = "phone"
            line_count +=1
        elif line_count == 3:
            ##This code seperates Device Id into a usuable format
            id = line.split()
            id = id[1]
            device_id = id.strip(",")
            device_id = device_id.strip("\"")
            device_id = device_id.strip("")
            line_count +=1
        elif line_count == 4:
            ##This code seperates event into usuable format
            id = line.split(":")
            id = id[1]
            event = id.strip(" ")
            event = event.replace(",", " ")
            event = event.replace("\""," ")
            event = event.rstrip()
            line_count +=1
        elif line_count == 5:
            ##This code gets the name of the person
            id = line.split(":")
            id = id[1]
            guest = id.replace("\"", " ")
            guest = guest.strip()
            if guest not in names:
                names[guest] = 0
                Individuals.append(guest)

            line_count +=1
            ##This code assigns the users data to an individual array along with a master array
            master_list.append(device)
            master_list.append(device_id)
            master_list.append(event)
            master_list.append(guest)
            if guest == "Rob":
                Rob.append(time)
                Rob.append(device)
                Rob.append(device_id)
                Rob.append(event)
                Rob.append(guest)
            if guest == "Veronica":
                Veronica.append(time)
                Veronica.append(device)
                Veronica.append(device_id)
                Veronica.append(event)
                Veronica.append(guest)
            if guest == "Jason":
                Jason.append(time)
                Jason.append(device)
                Jason.append(device_id)
                Jason.append(event)
                Jason.append(guest)
            if guest == "Thomas":
                Thomas.append(time)
                Thomas.append(device)
                Thomas.append(device_id)
                Thomas.append(event)
                Thomas.append(guest)
            if guest == "Kristina":
                Kristina.append(time)
                Kristina.append(device)
                Kristina.append(device_id)
                Kristina.append(event)
                Kristina.append(guest)
            if guest == "Marc-Andre":
                Marc_Andre.append(time)
                Marc_Andre.append(device)
                Marc_Andre.append(device_id)
                Marc_Andre.append(event)
                Marc_Andre.append(guest)
            if guest == "Dave":
                Dave.append(time)
                Dave.append(device)
                Dave.append(device_id)
                Dave.append(event)
                Dave.append(guest)
            if guest == "Salina":
                Salina.append(time)
                Salina.append(device)
                Salina.append(device_id)
                Salina.append(event)
                Salina.append(guest)
            if guest == "Harrison":
                Harrison.append(time)
                Harrison.append(device)
                Harrison.append(device_id)
                Harrison.append(event)
                Harrison.append(guest)
            if guest == "Eugene":
                Eugene.append(time)
                Eugene.append(device)
                Eugene.append(device_id)
                Eugene.append(event)
                Eugene.append(guest)
            if guest == "n/a":
                unknown.append(time)
                unknown.append(device)
                unknown.append(device_id)
                unknown.append(event)
                unknown.append(guest)
            if guest == "Alok":
                alok.append(time)
                alok.append(device)
                alok.append(device_id)
                alok.append(event)
                alok.append(guest)
            if guest == "n/a":
                na.append(time)
                na.append(device)
                na.append(device_id)
                na.append(event)
                na.append(guest)
    ##This line resets the count
    if line_count == 6:
        line_count = 0
    line = read.readline()

def check_room(searchEntry):
    #dev_room = input("Please Enter the device id or Room Number: ")
    check = False
    x = 2
    z = 4
    present = []
    freqs = {}
    while x < len(master_list):
        if searchEntry == master_list[x]:
            if master_list[z] not in freqs:
                freqs[master_list[z]] = master_list[z]
                present.append(" "+master_list[z]+" ")
            check = True
        x = x + 5
        z = z + 5
    if check == False:
        return("No ones in the room.")
    return (present)

def realatedtotime(varb):
    counter = 0
    for i in master_list:
        if i == varb:
            return ("Device : '" + str(master_list[counter+1]) + "' device ID : '"+ str(master_list[counter+2])+"' Event : '" + str(master_list[counter+3]) + "' By : '" + str(master_list[counter+4])+"'.")
        counter+=1

import tkinter as tk


# window = TK()
# window.title("test")

window = tk.Tk()
window.geometry("700x300")
window.title("Murder mystery")
window.resizable(False, False)
window.configure(background="light grey")

textoutput = tk.Label(window, text = "By: Andrew Hall, Atharva Kasture, Mitansh Desai, Spencer Low", bg="dark grey" ,fg="black", font=("Consolas",8,"bold"))
textoutput.place(x=100,y=230)
textoutput = tk.Label(window, text = "Our guess:\nJason murders Veronica", bg="dark grey" ,fg="black", font=("Consolas",8,"bold"))
textoutput.place(x=100,y=250)


def V_transfer():
    print("success")
    displayData(Veronica,0,"V")

def J_transfer():
    displayData(Jason,0,"J")

def T_transfer():
    displayData(Thomas,0,"T")

def R_transfer():
    displayData(Rob,0,"R")

def K_transfer():
    displayData(Kristina,0,"K")

def M_transfer():
    displayData(Marc_Andre,0,"M")

def D_transfer():
    displayData(Dave,0,"D")

def S_transfer():
    displayData(Salina,0,"S")

def H_transfer():
    displayData(Harrison,0,"H")

def E_transfer():
    displayData(Eugene,0,"E")

def A_transfer():
    displayData(alok,0,"A")

def N_transfer():
    displayData(na,0,"N")

def displayData(info,t,identifier):

    dataWindow = tk.Tk()
    dataWindow.title("Data window")
    dataWindow.geometry("630x620")
    dataWindow.resizable(False, False)
    dataWindow.configure(background="light grey")

    textToutput = tk.Label(dataWindow, text = "Time", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "flat",width=9)
    textToutput.grid(row=0,column=1)

    textToutput = tk.Label(dataWindow, text = "Device", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "raised",width=9)
    textToutput.grid(row=0,column=2)

    textToutput = tk.Label(dataWindow, text = "ID", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "sunken",width=9)
    textToutput.grid(row=0,column=3)

    textToutput = tk.Label(dataWindow, text = "Event", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "ridge",width=15)
    textToutput.grid(row=0,column=4)

    textToutput = tk.Label(dataWindow, text = "Guest ID", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "solid",width=9)
    textToutput.grid(row=0,column=5)

    textToutput = tk.Label(dataWindow, text = "EXTRA", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "groove")
    textToutput.grid(row=0,column=6)

    sampleGrid = tk.Label(dataWindow,text = "-------",borderwidth = 1, relief = "groove")
##This variable is used to run through the index of each list
    j = 0
    k = 0

    length = int(len(info)/5)
##Code to print out the proper info in the buttons
    print(length)
    if length == 1:
        length = 2
    for r in range(1,length+1):
        for c in range(1,6):
            if c ==4:
                sampleGrid = tk.Label(dataWindow,text = info[k],borderwidth = 1, relief = "groove",width=25)
                sampleGrid.grid(row=r,column=c)
                j += 1
                k += 1
                continue
            sampleGrid = tk.Label(dataWindow,text = info[k],borderwidth = 1, relief = "groove",width=15)
            sampleGrid.grid(row=r,column=c)
            j += 1
            k+=1
        if j > 5:
            j = 0
        if r == 30 or r == 60 or r == 90:
            dataWindow = tk.Tk()
            dataWindow.title("Data window")
            dataWindow.geometry("630x620")
            dataWindow.resizable(False, False)
            dataWindow.configure(background="light grey")

            textToutput = tk.Label(dataWindow, text = "Time", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "flat",width=9)
            textToutput.grid(row=0,column=1)

            textToutput = tk.Label(dataWindow, text = "Device", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "raised",width=9)
            textToutput.grid(row=0,column=2)

            textToutput = tk.Label(dataWindow, text = "ID", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "sunken",width=9)
            textToutput.grid(row=0,column=3)

            textToutput = tk.Label(dataWindow, text = "Event", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "ridge",width=15)
            textToutput.grid(row=0,column=4)

            textToutput = tk.Label(dataWindow, text = "Guest ID", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "solid",width=9)
            textToutput.grid(row=0,column=5)

            textToutput = tk.Label(dataWindow, text = "EXTRA", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "groove")
            textToutput.grid(row=0,column=6)

            # info = info[9:]



##hotel guests
###Veronica, Jason, Thomas, Rob, Kristina
textoutput = tk.Label(window, text = "Hotel guests", bg="dark grey" ,fg="black", font=("Felix Titling",16,"bold"))
textoutput.place(x=100,y=20)

testButton = tk.Button(text = "Veronica", command = V_transfer)
testButton.place(x=100,y=60)

testButton = tk.Button(text = "Jason", command = J_transfer)
testButton.place(x=100,y=100)
testButton = tk.Button(text = "Thomas", command = T_transfer )
testButton.place(x=100,y=140)
testButton = tk.Button(text = "Rob", command = R_transfer)
testButton.place(x=100,y=180)
testButton = tk.Button(text = "Kristina", command = K_transfer)
testButton.place(x=100,y=180)


##hotel staff
###Marc-Andre,Dave,Salina,Harrison
textoutput = tk.Label(window, text = "Hotel staff", bg="dark grey" ,fg="black", font=("Felix Titling",16,"bold"))
textoutput.place(x=300,y=20)

testButton = tk.Button(text = "Marc-Andre", command = M_transfer)
testButton.place(x=300,y=60)
testButton = tk.Button(text = "Dave", command = D_transfer)
testButton.place(x=300,y=100)
testButton = tk.Button(text = "Salina", command = S_transfer)
testButton.place(x=300,y=140)
testButton = tk.Button(text = "Harrison", command = H_transfer)
testButton.place(x=300,y=180)

##random people
###eugune???
textoutput = tk.Label(window, text = "Unidentified", bg="dark grey" ,fg="black", font=("Felix Titling",16,"bold"))
textoutput.place(x=480,y=20)

testButton = tk.Button(text = "Eugene", command = E_transfer)
testButton.place(x=480,y=60)
testButton = tk.Button(text = "Alok", command = A_transfer)
testButton.place(x=480,y=100)
testButton = tk.Button(text = "N/A", command = N_transfer)
testButton.place(x=540,y=100)


textoutput = tk.Label(window, text = "Room or Time", bg="dark grey" ,fg="black", font=("Felix Titling",16,"bold"))
textoutput.place(x=450,y=150)

userEntry = tk.Entry(window)
userEntry.place(x=500,y=200)


def searchClick():
    #SEARCH ENTRY STORES THE USER INPUT<--------------------------------------------------
    searchEntry = userEntry.get()
    if searchEntry.isdigit() and len(searchEntry) > 3:
        input = realatedtotime(searchEntry)
    else:
        input = check_room(searchEntry)
    searchWindow = tk.Tk()
    searchWindow.title("Search Window")
    searchWindow.geometry("900x85")
    searchWindow.resizable(False, False)
    searchWindow.configure(background="light grey")
    textToutput = tk.Label(searchWindow, text = input,fg ="black", font=("Felix Titling",10,"bold"), borderwidth = 15, relief = "flat",width=90)
    textToutput.grid(row=0,column=3)
    # tk.Text


#a button that uses the function above
tk.Button(window,text="SEARCH",command=searchClick).place(x=445,y=200)

print(Marc_Andre)


window.mainloop()
