# Aufgabe "Max"-Anzahl zählen

import os

print("\nHier gehts los:")
folder = os.path.join(os.path.dirname(__file__), "names")
print(folder)
#print(os.listdir("names"))
filelist = os.listdir(folder)
#print(filelist)

counter = 0

for item in filelist:
    filename = os.path.join(folder, item)
    #print(filename)
    #print(folder)
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            seperated_line = line.split()
            #print(seperated_line)
            if seperated_line[0] == "Max":
                counter = counter + 1

print("Max kommt: " + str(counter) + "x vor!")


#filename = os.path.join(os.path.dirname(__file__), "ordner")
#print(filename)