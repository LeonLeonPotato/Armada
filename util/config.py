import util.utils
import json

initiated = False
cfg : dict

preset_name : str
preset : dict

name : str
id : str
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

    name = main["name"]
    id = main["id"]
    level = main["level"]
    uid = main["uid"]
    exp = main["exp"]
    orundums = main["orundums"]
    primes = main["primes"]
    lmd = main["lmd"]
    assistant = main["assistant"]
    skin = main["skin"]

    initiated = True

    