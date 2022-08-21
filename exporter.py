from char.char_manager import findByFullName
import utils.utils as utils
import json
from char.character import Character
import char.char_manager

out = {}

i : Character
for i in char.char_manager.char_list:
    st : str = ""
    ap : str = "0"
    if(i.rarity >= 4):
        ap = "3"
    for i0 in range(0, i.skillCount()):
        st += ap

    module = None
    if(len(i.modules) >= 1):
        module = i.modules[-1]

    op = {
        "elite": i.maxpromotion,
        "level": i.maxlevel,
        "potential": 6,
        "module": module,
        "skin": 2,
        "skillLevel": 7,
        "mainSkill": i.skillCount(),
        "masteries": st
    }
    
    out[i.fullname] = op

utils.cf("presets/generic_cc.json", json.dumps(out, indent=4))

