from character import Character

import os
import json

modTemp = "{\"result\":0,\"playerDataDelta\":{\"modified\":{\"troop\":{\"chars\":{\"{0}\":{\"instId\":{0},\"charId\":\"char_222_bpipe\",\"favorPoint\":25570,\"potentialRank\":0,\"mainSkillLvl\":7,\"skin\":\"char_222_bpipe@race#1\",\"level\":60,\"exp\":114,\"evolvePhase\":2,\"defaultSkillIndex\":2,\"gainTime\":1646300758,\"skills\":[{\"skillId\":\"skcom_quickattack[3]\",\"unlock\":1,\"state\":0,\"specializeLevel\":0,\"completeUpgradeTime\":-1},{\"skillId\":\"skchr_bpipe_2\",\"unlock\":1,\"state\":0,\"specializeLevel\":0,\"completeUpgradeTime\":-1},{\"skillId\":\"skchr_bpipe_3\",\"unlock\":1,\"state\":0,\"specializeLevel\":2,\"completeUpgradeTime\":-1}],\"currentEquip\":\"uniequip_002_bpipe\",\"equip\":{\"uniequip_001_bpipe\":{\"hide\":0,\"locked\":0,\"level\":1},\"uniequip_002_bpipe\":{\"hide\":0,\"locked\":0,\"level\":1}},\"voiceLan\":\"JP\"}}}},\"deleted\":{}}}"char_table = json.load(open("cache/char_table.json", "r", encoding="utf-8"))
# char_list = []
# module_table = json.load(open("cache/mod_table.json", "r", encoding="utf-8"))
# module_list = []

# for n, i in char_table.items():
#     if(n.startswith("char")):
#         char_list.append(Character(n, i["rarity"] + 1, i["phases"][-1]["maxLevel"], len(i["phases"])))

# for n, i in module_table["equipDict"].items():
#     pass

# def isAKServer(st: str) -> bool:
#     return st.find("arknights") != -1

# def findCharFromModule(st: str) -> Character:
#     for i in char_list:
#         pass



def cfd(name: str) -> bool:
    returnval = not os.path.exists(name)
    if(returnval):
        os.makedirs(name)
    return returnval

def cf(name: str, content = "") -> bool:
    with open(name, "wb") as file:
        file.write(content.encode("utf-8"))

def rf(name: str) -> str:
    with open(name, "r", encoding="utf-8") as file:
        return file.read()
