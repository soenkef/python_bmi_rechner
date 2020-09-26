import os

print(__file__)
print(os.path.dirname(__file__))

# alle Dateien im aktuellen Pfad ausgeben

with open(os.path.join(os.path.dirname(__file__), "datei.txt")) as file:
    for line in file:
        print(line)

print(os.listdir("."))