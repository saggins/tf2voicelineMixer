from multiprocessing import connection
import sqlite3
from tracemalloc import start
from models import Phoneme, Word

phonemeTable = """
CREATE TABLE IF NOT EXISTS phoneme (
    class char(10) NOT NULL,
    phoneme char(4) NOT NULL,
    word char (100) NOT NULL,
    soundFilePath char(100) NOT NULL,
    startMS int(10) NOT NULL,
    endMS int (10) NOT NULL    
);
"""

wordTable = """
CREATE TABLE IF NOT EXISTS words (
    class char(10) NOT NULL,
    word char(100) NOT NULL,
    soundFilePath char(100) NOT NULL,
    startMS int(10) NOT NULL,
    endMS int (10) NOT NULL
"""
allSQLtables = [phonemeTable, wordTable]
def getConn() -> sqlite3.Connection:
    return sqlite3.connect('audio.sqlite')

def startup():
    conn = getConn()
    for sql in allSQLtables:
        conn.execute(sql)
startup()

def addPhoneme(phoneme: Phoneme):
    sql_addPhoneme = """
        INSERT INTO phoneme (class, phoneme, word, soundFilePath, startMS, endMS)
        VALUES (?, ?, ?, ?, ?, ?);
    """
    getConn().execute(sql_addPhoneme, (phoneme.class_, phoneme.phoneme, phoneme.word, phoneme.soundFilePath, phoneme.startMS, phoneme.endMS))

def addWord (word : Word):
    sql_addWord = """
        INSERT INTO word (class, word, soundFilePath, startMS, endMS)
        VALUES (?, ?, ?, ?, ?);
    """
    getConn().execute(sql_addWord, (word.class_, word.phoneme, word.word, word.soundFilePath, word.startMS, word.endMS))