import mitmproxy.http
import json
import utils.utils as utils
from char.character import Character
from char.char_manager import *

def request(flow: mitmproxy.http.HTTPFlow):
    if(flow.request.path != "/account/syncData"): 
        return

def response(flow: mitmproxy.http.HTTPFlow):
    if(flow.request.path != "/account/syncData"): 
        return

    og = json.loads(flow.response.text)
    chars = og["user"]["troop"]["chars"]

    for i, c in chars.items():
        char : Character = findByFullName(c["charId"])
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

                


