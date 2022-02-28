from tokenize import Number
from pydub import AudioSegment


"""
What thsi sdoes

Takes fiel and extrtascts from starts ec and endsecc
"""
def extractSound (filename: str, startsec : Number, endsec : Number):
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
    sound[-(durationms-startms):endms].export(f"./out.{extension}", format=extension)

extractSound("Scout item unicorn domination01.wav", 0, 1)