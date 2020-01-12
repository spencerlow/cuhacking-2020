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

#yeet
Rob = []
Veronica = []
Jason = []
Thomas = []
Kristina = []
Marc_Andre = []
Dave = []
Salina = []
Harrison = []

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
            print(time)
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
            print(device)
        elif line_count == 3:
            ##This code seperates Device Id into a usuable format
            id = line.split()
            id = id[1]
            device_id = id.strip(",")
            device_id = device_id.strip("\"")
            device_id = device_id.strip("")
            line_count +=1
            print(device_id)
        elif line_count == 4:
            ##This code seperates event into usuable format
            id = line.split(":")
            id = id[1]
            event = id.strip(" ")
            event = event.replace(",", " ")
            event = event.replace("\""," ")
            event = event.rstrip()
            line_count +=1
            print(event)
        elif line_count == 5:
            ##This code gets the name of the person
            id = line.split(":")
            id = id[1]
            guest = id.replace("\"", " ")
            guest = guest.strip()
            line_count +=1
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

    ##This line resets the count
    if line_count == 6:
        line_count = 0
    line = read.readline()

print(Rob)
print(Veronica)
