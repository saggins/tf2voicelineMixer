"""
This is proabbly written wrong.

taking IPA to gentle api's CMU pronoucing stuff (35 arpabet)
Kek
"""
#Copied from https://github.com/willianantunes/transcriber-wrapper/blob/main/transcriber_wrapper/dealers/InternationalPhoneticAlphabet.py
us_phone_set_to_ipa = {
        "ɑ" : "aa",
        "æ" : "ae",
        "ə" : "ah",
        "ɔ" : "ao",
        "aʊ": "aw", # here
        "ax": "ə",
        "ay": "aɪ",
        "eh": "ɛ",
        "el": "l̩",
        "em": "m̩",
        "en": "n̩",
        "er": "ər",
        "ey": "eɪ",
        "ih": "ɪ",
        "iy": "i",
        "ow": "oʊ",
        "oy": "ɔɪ",
        "uh": "ʊ",
        "uw": "u",
        "b": "b",
        "ch": "ʧ",
        "d": "d",
        "dh": "ð",
        "f": "f",
        "g": "ɡ",
        "hh": "h",
        "jh": "ʤ",
        "k": "k",
        "l": "l",
        "m": "m",
        "n": "n",
        "ng": "ŋ",
        "p": "p",
        "r": "ɹ",
        "s": "s",
        "sh": "ʃ",
        "t": "t",
        "th": "θ",
        "v": "v",
        "w": "w",
        "y": "j",
        "z": "z",
        "zh": "ʒ",
        "pau": "",
    }
def ipaToArpabet():

