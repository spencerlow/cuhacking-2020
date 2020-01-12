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
unknown = []
master_list =[]

def timetoepoch():
    zeinput = input("Input time in format YYYY-MM-DD HH:MM:SS ")
    import calendar, time; return (calendar.timegm(time.strptime(zeinput, '%Y-%m-%d %H:%M:%S')))

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
            master_list.append(time)
            master_list.append(device)
            master_list.append(device_id)
            master_list.append(event)
            master_list.append(guest)
            if guest == "Rob":
                Rob.append(time)
                Rob.append(device)
                Rob.append(device_id)
                Rob.append(event)
            if guest == "Veronica":
                Veronica.append(time)
                Veronica.append(device)
                Veronica.append(device_id)
                Veronica.append(event)
            if guest == "Jason":
                Jason.append(time)
                Jason.append(device)
                Jason.append(device_id)
                Jason.append(event)
            if guest == "Thomas":
                Thomas.append(time)
                Thomas.append(device)
                Thomas.append(device_id)
                Thomas.append(event)
            if guest == "Kristina":
                Kristina.append(time)
                Kristina.append(device)
                Kristina.append(device_id)
                Kristina.append(event)
            if guest == "Marc_Andre":
                Marc_Andre.append(time)
                Marc_Andre.append(device)
                Marc_Andre.append(device_id)
                Marc_Andre.append(event)
            if guest == "Dave":
                Dave.append(time)
                Dave.append(device)
                Dave.append(device_id)
                Dave.append(event)
            if guest == "Salina":
                Salina.append(time)
                Salina.append(device)
                Salina.append(device_id)
                Salina.append(event)
            if guest == "Harrison":
                Harrison.append(time)
                Harrison.append(device)
                Harrison.append(device_id)
                Harrison.append(event)
            if guest == "Eugene":
                Eugene.append(time)
                Eugene.append(device)
                Eugene.append(device_id)
                Eugene.append(event)
            if guest == "n/a":
                unknown.append(time)
                unknown.append(device)
                unknown.append(device_id)
                unknown.append(event)
            if guest == "Alok":
                alok.append(time)
                alok.append(device)
                alok.append(device_id)
                alok.append(event)
    ##This line resets the count
    if line_count == 6:
        line_count = 0
    line = read.readline()

dev_room = input("Please Enter the device id or Room Number: ")
check = False
x = 2
z = 4
present = []
freqs = {}
while x < len(master_list):
    if dev_room == master_list[x]:
        if master_list[z] not in freqs:
            freqs[master_list[z]] = master_list[z]
            present.append(master_list[z])
        check = True
    x = x + 5
    z = z + 5
if check == False:
    print("No ones in the room.")
print (present)

def realatedtotime():
    varb = input("Enter the time in epoch: ")
    for i in master_list:
        if i == varb:
            return ("The device was " + (i+1) +" with device id: "+(i+2)+". The event was "+(i+3)+", and person involved was "+(i+4)+".")

import tkinter as tk


# window = TK()
# window.title("test")

window = tk.Tk()
window.geometry("700x250")
window.title("Murder mystery")
window.resizable(False, False)
window.configure(background="light grey")

def V_transfer():
    displayData(Veronica)

def J_transfer():
    displayData(Jason)

def T_transfer():
    displayData(Thomas)

def R_transfer():
    displayData(Rob)

def K_transfer():
    displayData(Kristina)

def M_transfer():
    displayData(Marc_Andre)

def D_transfer():
    displayData(Dave)

def S_transfer():
    displayData(Salina)

def H_transfer():
    displayData(Harrison)

def E_transfer():
    displayData(Eugene)

def N_transfer():
    displayData(n/a)

def A_transfer():
    displayData(alok)



def T_transfer():
    displayData(Thomas)


def displayData(info):
    text = "test text here"
    dataWindow = tk.Tk()
    dataWindow.title("Data window")
    dataWindow.geometry("630x400")
    dataWindow.resizable(False, False)
    dataWindow.configure(background="light grey")


    textToutput = tk.Label(dataWindow, text = "Time", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "flat",width=9)
    textToutput.grid(row=0,column=1)

    textToutput = tk.Label(dataWindow, text = "Device", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "raised",width=9)
    textToutput.grid(row=0,column=2)

    textToutput = tk.Label(dataWindow, text = "Device ID", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "sunken",width=9)
    textToutput.grid(row=0,column=3)

    textToutput = tk.Label(dataWindow, text = "Event", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "ridge",width=15)
    textToutput.grid(row=0,column=4)

    textToutput = tk.Label(dataWindow, text = "Guest ID", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "solid",width=9)
    textToutput.grid(row=0,column=5)

    textToutput = tk.Label(dataWindow, text = "EXTRA", fg="red", font=("Helvetica",16),borderwidth = 1, relief = "groove")
    textToutput.grid(row=0,column=6)

    sampleGrid = tk.Label(dataWindow,text = "-------",borderwidth = 1, relief = "groove")


    j = 0
    for r in range(1,10):
        for c in range(1,6):
            #if column is EVENT, have the width as larger since it needs more space, continue to next iteration
            if c ==4:
                sampleGrid = tk.Label(dataWindow,text = info[j],borderwidth = 1, relief = "groove",width=25)
                sampleGrid.grid(row=r,column=c)
                j += 1
                continue
            sampleGrid = tk.Label(dataWindow,text = info[j],borderwidth = 1, relief = "groove",width=15)
            sampleGrid.grid(row=r,column=c)
            j += 1
        if j > 5:
            j = 0


#Groups

##hotel guests
###Veronica, Jason, Thomas, Rob, Kristina
textoutput = tk.Label(window, text = "Hotel guests", bg="dark grey" ,fg="black", font=("Felix Titling",16,"bold"))
textoutput.place(x=100,y=20)

testButton = tk.Button(text = "Veronica", command = V_transfer)
testButton.place(x=100,y=60)

testButton = tk.Button(text = "Jason", command = J_transfer)
testButton.place(x=100,y=100)
testButton = tk.Button(text = "Thomas", command = T_transfer)
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

window.mainloop()

# if __name__ == "__main__":
#     window.mainloop()
