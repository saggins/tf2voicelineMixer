"""
What thsi does ,

is get's trasncript from JSON FILE from extract.py
then feedxcs it gentl restapi and puts data to sqlite datbase
"""
import json
from typing import Dict, List
import requests
from audio import extractSound

from models import Phoneme, Word

def getData (name: str,voiceLine: str):
    path = f"./sounds/{name}"
    results = None
    listOWords = []
    listOPhomeme = []
    with open(path, 'rb') as sound:
        results = requests.post(f"{gentleAPI}/transcriptions?async=false", files={'audio': sound, 'transcript':voiceLine}).json()
    for r in results["words"]:
        if (r["case"] == "success") :
            #TODO Words
            #FIXME class name scout
            word = Word(class_= 'scout', word=r['alignedWord'], soundFilePath=name, startMS=r["start"], endMS=r['end']) 
            listOWords.append(word)
            #TODO Phonemes
            phomemeStartSec = float(r["start"])
            for pr in r["phones"]:
                #FIXME fix scout
                phomemeEndSec = round (((phomemeStartSec + float(pr["duration"])) *1000))
                phomeme = Phoneme(class_='scout',phoneme=pr['phone'], word=word.word, soundFilePath=name, startMS=phomemeStartSec, endMS=phomemeEndSec)
                listOPhomeme.append(phomeme)
                phomemeStartSec = phomemeEndSec
    return {"words": listOWords, "phomes": listOPhomeme}

pathTofile= "./scoutsoundreference.json"
gentleAPI = "http://localhost:8765"

f = open(pathTofile)

soundData = json.load(f)
# for entry in soundData["sounds"]:
#     getPhonemes(entry['name'], entry['voiceLine'] )
entry = soundData["scout"][0]
dataList = getData(entry['name'], entry['voiceLine'])

for word in dataList['words']:
    print(word)
for phome in dataList['phomes']:
    print(phome)