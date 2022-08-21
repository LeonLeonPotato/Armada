from util.char.character import Character
import json

initiated = False

char_table = None
char_list = []

module_table = None

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
    char_table = json.load(open("cache/char_table.json", "r", encoding="utf-8"))
    module_table = json.load(open("cache/mod_table.json", "r", encoding="utf-8"))
    char_list = []

    for i, c in char_table.items():
        if(i.startswith("char")):
            skills = []

            for c0 in c["skills"]:
                skills.append(c0["skillId"])

            char_list.append(Character(
                i, 
                c["rarity"] + 1, 
                c["phases"][-1]["maxLevel"], 
                len(c["phases"]) - 1, 
                skills
            ))

    for i, c in module_table["charEquip"].items():
        cha : Character = findByFullName(i)
        cha.modules = c
        
    initiated = True
    