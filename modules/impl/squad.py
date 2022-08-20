import mitmproxy.http
import json
import utils
from character import Character

char_table = json.load(open("cache/char_table.json", "r", encoding="utf-8"))
char_list = []
module_table = json.load(open("cache/mod_table.json", "r", encoding="utf-8"))
module_list = []

for n, i in char_table.items():
    if(n.startswith("char")):
        char_list.append(Character(n, i["rarity"] + 1, i["phases"][-1]["maxLevel"], len(i["phases"]) - 1))

# for n, i in module_table["equipDict"].items():
#     pass

def findByName(fullname: str) -> Character:
    n: Character
    for n in char_list:
        if(n.fullname == fullname):
            return n
    return None

def findCharFromModule(st: str) -> Character:
    for i in char_list:
        pass


def request(flow: mitmproxy.http.HTTPFlow):
    if(flow.request.path != "/account/syncData"): 
        return

def response(flow: mitmproxy.http.HTTPFlow):
    if(flow.request.path != "/account/syncData"): 
        return

    og = json.loads(flow.response.text)
    chars = og["user"]["troop"]["chars"]

    for i, c in chars.items():
        char : Character = findByName(c["charId"])
        c["favorPoint"] = 25570
        c["evolvePhase"] = char.maxpromotion
        c["level"] = char.maxlevel
        c["potentialRank"] = 5
        if(char.rarity >= 3):
            c["mainSkillLvl"] = 7

        for c1 in c["skills"]:
            c1["unlock"] = 1
            c1["specializeLevel"] = 3

        og["user"]["troop"]["chars"][str(i)] = c

    flow.response.set_text(json.dumps(og))

                


