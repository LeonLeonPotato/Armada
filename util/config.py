import util.utils
import json

initiated = False

cfg : dict

preset_name : str
preset : dict

def initiate():
    global cfg
    global preset_name
    global preset

    cfg = json.loads(util.utils.rf("config.json"))
    preset_name = cfg["main"]["preset"]
    preset = json.loads(util.utils.rf("presets/" + preset_name))

if not initiated:
    initiate()
    initiated = True

    