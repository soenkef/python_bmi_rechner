print("BMI-Rechner")

weight = input("Bitte gebe dein Gewicht in KG wie z.B. 84.2 kg ein: ")
height = input("Bitte gebe deine Körpergröße im Meter wie z.B. 1.82 ein: ")

result = (float(weight.replace(",", ".")) / (float(height.replace(",", ".")) ** 2))

print("Dein BMI liegt bei: " + str(round(result, 1)))