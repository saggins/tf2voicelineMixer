from lib2to3.pytree import Base
from pydantic import BaseModel

class Phoneme (BaseModel):
    class_ : str
    phoneme: str
    soundFilePath: str
    startMS: str
    endMS: str

class Word(BaseModel): 
    class_ : str
    word: str
    soundFilePath: str
    startMS: str
    endMS: str