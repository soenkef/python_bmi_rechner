import os

#print(__file__)
#pint(os.path.dirname(__file__))
print("Hier gehts los: ")
print(__file__)
print(os.path.join(os.path.dirname(__file__), "datei.txt"))

# alle Dateien im aktuellen Pfad ausgeben

with open(os.path.join(os.path.dirname(__file__), "datei.txt"), "r") as file:
    for line in file:
        print(line)

print(os.listdir("."))