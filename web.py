from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from models import Phoneme, Word, UserInput
app = FastAPI()

app.mount('/', StaticFiles(directory='./web/public', html=True), name="web")

@app.post("/userinput/")
async def handleUser(input: UserInput):
    #TODO This function in brains; make do brainstuff
    #TODO Need to report to data.py
    #TODO Need to analze phome in this function
    #TODO Need to return Phome models, word models to client  