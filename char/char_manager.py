from char.character import Character
import json

initiated = False

char_table = None
char_list = []

module_table = None

def initiate():
    global char_table
    global module_table
    global char_list
    
    char_table = json.load(open("cache/char_table.json", "r", encoding="utf-8"))
    module_table = json.load(open("cache/mod_table.json", "r", encoding="utf-8"))
    char_list = []

    for n, i in char_table.items():
        if(n.startswith("char")):
            char_list.append(Character(n, i["rarity"] + 1, i["phases"][-1]["maxLevel"], len(i["phases"]) - 1))

    for n, i in module_table["charEquip"].items():
        cha : Character = findByFullName(n)
        cha.modules = i

def findByName(st : str) -> Character:
    i:Character
    for i in char_list:
        if(i.name == st):
            return i
    return None

def findByFullName(st : str) -> Character:
    i:Character
    for i in char_list:
        if(i.fullname == st):
            return i
    return None

def findCharByModule(mod : str) -> Character:
    i:Character
    for i in char_list:
        if(mod in i.modules):
            return i
    return None

if not initiated:
    initiate()
    initiated = True
    