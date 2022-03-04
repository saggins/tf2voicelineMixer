from tokenize import Number
from pydub import AudioSegment

from models import Word


"""
What thsi sdoes

Takes fiel and extrtascts from starts ec and endsecc
"""
def extractSound (word: Word) -> AudioSegment:
    filename = word.soundFilePath
    startsec = float(word.startMS) #Fixme
    endsec = float(word.endMS)

    extension = filename.split(".")[1]
    startms = startsec*1000
    endms = endsec*1000 
    
    match extension:
        case "wav":
            sound = AudioSegment.from_wav(f"./sounds/{filename}")
        case "mp3":
            sound = AudioSegment.from_mp3(f"./sounds/{filename}")
        case _:
            sound = AudioSegment.from_file(f"./sounds/{filename}", extension)
    
    durationms = sound.duration_seconds*1000
    return sound[-(durationms-startms):endms].export(f"./out.{extension}", format=extension)
