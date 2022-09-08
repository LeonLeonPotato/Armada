import modules.impl.battle
import modules.impl.menu
import modules.impl.squad
import modules.impl.crisis
import modules.impl.stage
import modules.impl.story
import modules.impl.assist
import modules.impl.replay

requests = []
responses = []

logs = []

def add(mod):
    global requests
    global responses

    requests = requests + mod.requests
    responses = responses + mod.responses

add(modules.impl.menu)
add(modules.impl.battle)
add(modules.impl.squad)
add(modules.impl.crisis)
add(modules.impl.stage)
add(modules.impl.story)
add(modules.impl.assist)
add(modules.impl.replay)

logs.append(["/crisis/getInfo", "crisis"])
logs.append(["/account/syncStatus", "syncStatus"])
logs.append(["/account/syncData", "syncData"])
logs.append(["/crisis/battleStart", "crisisBattle"])