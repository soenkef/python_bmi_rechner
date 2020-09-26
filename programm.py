print("BMI-Rechner")

weight = input("Bitte gebe dein Gewicht in KG wie z.B. 84.2 kg ein: ")
height = input("Bitte gebe deine Körpergröße im Meter wie z.B. 1.82 ein: ")

result = (float(weight) / (float(height) * float(height)))

print("Dein BMI liegt bei: " + str(result))