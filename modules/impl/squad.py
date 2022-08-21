import mitmproxy.http
import json
from util.char.character import Character
from util.char.char_manager import *

import util.config

def request(flow: mitmproxy.http.HTTPFlow):
    if(flow.request.path != "/account/syncData"): 
        return

def response(flow: mitmproxy.http.HTTPFlow):
    if(flow.request.path != "/account/syncData"): 
        return

    og = json.loads(flow.response.text)
    # chars = og["user"]["troop"]["chars"]

    # for i, c in chars.items():
    #     char : Character = findByFullName(c["charId"])
    #     c["favorPoint"] = 25570
    #     c["evolvePhase"] = char.maxpromotion
    #     c["level"] = char.maxlevel
    #     c["potentialRank"] = 5
    #     if(char.rarity >= 3):
    #         c["mainSkillLvl"] = 7

    #     for c1 in c["skills"]:
    #         c1["unlock"] = 1
    #         c1["specializeLevel"] = 3

    #     og["user"]["troop"]["chars"][str(i)] = c

    out = {}

    index = 0
    for i, c in util.config.preset.items():
        index += 1
        char = findByFullName(i)
        char_cfg = util.config.preset[i]

        mastery_pastern : str = char_cfg["masteries"]
        skills = []
        for idx, c0 in enumerate(char.skills):
            skills.append({
                "skillId": c0,
                "unlock": 1,
                "state": 0,
                "specializeLevel": mastery_pastern[idx],
                "completeUpgradeTime": -1
            })

        equipment = {}
        for c0 in char.modules:
            equipment[c0] = {
                "hide": 0,
                "locked": 0,
                "level": 1
            }

        op = {
            "instId": index,
            "charId": i,
            "favorPoint": c["trust"],
            "potentialRank": c["potential"] - 1,
            "mainSkillLvl": c["skillLevel"],
            "skin": i + "#" + str(c["skin"]),
            "level": c["level"],
            "exp": 0,
            "evolvePhase": c["elite"],
            "defaultSkillIndex": c["mainSkill"] - 1,
            "gainTime": index * 1000,
            "skills": skills,
            "voiceLan": "JP", # implement other voices later
            "currentEquip": c["module"],
            "equip": equipment
        }

        out[str(index)] = op

    og["user"]["troop"]["chars"] = out

    flow.response.set_text(json.dumps(og))

                


