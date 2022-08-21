import modules.impl.battle
import modules.impl.menu
import modules.impl.squad

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

logs.append(["/crisis/getInfo", "crisis"])
logs.append(["/account/syncStatus", "syncStatus"])
logs.append(["/account/syncData", "syncData"])