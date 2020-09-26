# Programmen Parameter übergeben
#c:\Users\Albert\Documents\#Fernstudium\udemy\Python Bootcamp udemy\Kursmaterialien\PythonProject>C:\Users\Albert\Anaconda3\python.exe argv.py "C:\Users\Albert\Documents\#Fernstudium\udemy\Python Bootcamp udemy\Kursmaterialien\PythonProject\datei.txt"

import sys

#print(sys.argv)

if len(sys.argv) >= 2:
    filename = sys.argv[1]

    file = open(filename, "r")
    counter = 0

    for line in file:
        counter = counter + 1

    print(counter)

else:
    print("Filename missing")