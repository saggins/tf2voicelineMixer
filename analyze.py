"""
What thsi does ,

is get's trasncript from JSON FILE from extract.py
then feedxcs it gentl restapi and puts data to sqlite datbase
"""
import json
from tracemalloc import start
from typing import List
import requests

from models import Phoneme, Word

def getData (name: str,voiceLine: str) -> List[Phoneme, Word]:
    path = f"./sounds/{name}"
    results = None
    with open(path, 'rb') as sound:
        results = requests.post(f"{gentleAPI}/transcriptions?async=false", files={'audio': sound, 'transcript':voiceLine}).json()
    for r in results["words"]:
        #Words
        getWord(r)
        #Phonemes
        pass

def getWord (result) -> Word:
    if (not result["case"] == "success") :
        return None
    #FIXME Scout prob
    return Word(class_= 'scout', word=result['alignedWord'], soundFilePath="test", startMS=result["start"], endMS=result['end']) 
pathTofile= "./scoutsoundreference.json"
gentleAPI = "http://localhost:8765"

f = open(pathTofile)

soundData = json.load(f)
# for entry in soundData["sounds"]:
#     getPhonemes(entry['name'], entry['voiceLine'] )
entry = soundData["sounds"][0]
print(getData(entry['name'], entry['voiceLine'] ).text)
