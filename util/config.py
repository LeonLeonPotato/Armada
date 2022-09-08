import util.utils
import json
import os

initiated = False
cfg : dict

preset_name : str
preset : dict
replays_name : str
replays : dict

name : str
tag : str
uid : int
level : int
exp : int
assistant : str
skin : int
orundums : int
primes : int
lmd : int

if not initiated:
    cfg = json.loads(util.utils.rf("config.json"))

    main = cfg["main"]

    preset_name = main["preset"]
    preset = json.loads(util.utils.rf("presets/" + preset_name))

    replays_name = preset_name.replace(".json", "") + "_replays.json"
    if(os.path.exists("presets/" + replays_name)):
        replays = json.loads(util.utils.rf("presets/" + replays_name))
    else:
        replays = {}
        util.utils.cf("presets/" + replays_name, r"{}")

    name = main["name"]
    tag = main["id"]
    level = main["level"]
    uid = main["uid"]
    exp = main["exp"]
    orundums = main["orundums"]
    primes = main["primes"]
    lmd = main["lmd"]
    assistant = main["assistant"]
    skin = main["skin"]

    initiated = True