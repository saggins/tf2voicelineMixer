from genericpath import exists
import json
from bs4 import BeautifulSoup
import requests
import re

"""
    What tist tdoes, 
    Extracts file / trnascritp from wiki page ( sry)

    and saves to file
"""

gentleurl = "127.0.0.1:8765"
extractingURL = ["https://wiki.teamfortress.com/wiki/Scout_responses", "https://wiki.teamfortress.com/wiki/Soldier_responses"]
soundTranscript = []
classes = ["scout", "soldier", "pyro", "demoman", "heavy", "engineer", "medic", "sniper", "spy"]

choice = input ("from (1-9) please choose which class you want to pick")
choice = int(choice)-1

r = requests.get(extractingURL[choice])
soup = BeautifulSoup(r.text, "html.parser")

voicelineRE = re.compile(".*\/w\/images\/.*")
voiceline = soup.find_all("a", class_="internal",href=voicelineRE  )

for line in voiceline :
    href = line["href"]
    content = line.string
    name  = line ["title"]
    path = f'./sounds/{name}'

    if (not exists(path)):
        print ("requesting File \n")
        classSound = requests.get( "https://wiki.teamfortress.com/" + href )

        print (f"writing {name} \n")
        f = open( path, 'wb')
        f.write(classSound.content)
        f.close()
    soundTranscript.append({"name": name, "voiceLine": content})

with open(f"{classes[choice]}soundreference.json", "w") as outfile:
    json.dump({ classes[choice]: soundTranscript}, outfile)
print(soundTranscript)