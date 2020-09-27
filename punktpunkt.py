import os

folder = os.path.join(os.path.dirname(__file__), "ordner/unterordner")

print(os.listdir("."))
#print(folder)

print(os.listdir(folder))

for file in os.listdir(folder):
    filepath = os.path.join(folder, file)
    if os.path.isdir(filepath):
        print(file + " ist ein Ordner")
    else:
        print(file + " ist eine Datei")


print(filepath)