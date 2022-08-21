from util.char.char_manager import findByFullName
import util.utils as utils
import json
from util.char.character import Character
import util.char.char_manager

out = {}

i : Character
for i in util.char.char_manager.char_list:
    st : str = ""
    ap : str = "0"
    if(i.rarity >= 4):
        ap = "3"
    for i0 in range(0, i.skillCount()):
        st += ap

    module = None
    if(len(i.modules) >= 1):
        module = i.modules[-1]

    skin = 1
    if(i.maxpromotion == 2):
        skin = 2

    op = {
        "elite": i.maxpromotion,
        "level": i.maxlevel,
        "trust": 25570,
        "potential": 6,
        "module": module,
        "skin": skin,
        "skillLevel": 7,
        "mainSkill": i.skillCount(),
        "masteries": st
    }
    
    out[i.fullname] = op

utils.cf("presets/generic_cc.json", json.dumps(out, indent=4))

