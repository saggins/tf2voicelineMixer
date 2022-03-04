from lib2to3.pytree import Base
from pydantic import BaseModel

class Phoneme (BaseModel):
    class_ : str
    phoneme: str
    word: str
    soundFilePath: str
    startMS: float
    endMS: float

class Word(BaseModel): 
    class_ : str
    word: str
    soundFilePath: str
    startMS: str
    endMS: str

class UserInput(BaseModel):
    class_: str
    userInput: str