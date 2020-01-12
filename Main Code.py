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

def timetoepoch():
    zeinput = input("Input time in format YYYY-MM-DD HH:MM:SS: ")
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
        ##This code assigns the users data to an individual array
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
            if guest == "Marc_Andre":
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
    ##This line resets the count
    if line_count == 6:
        line_count = 0
    line = read.readline()
print(Individuals)
