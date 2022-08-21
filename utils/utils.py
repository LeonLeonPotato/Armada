from char.character import Character

import os
import json

def isAKServer(st: str) -> bool:
     return st.find("arknights") != -1

def cfd(name: str) -> bool:
    returnval = not os.path.exists(name)
    if(returnval):
        os.makedirs(name)
    return returnval

def cf(name: str, content = "") -> bool:
    with open(name, "wb") as file:
        if(content is bytes):
            file.write(content)
        else:
            file.write(content.encode("utf-8"))

def rf(name: str) -> str:
    with open(name, "r", encoding="utf-8") as file:
        return file.read()
