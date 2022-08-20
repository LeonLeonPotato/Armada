import modules.impl.battle

requests = []
responses = []

logs = []

def add(mod):
    requests.append(mod.request)
    responses.append(mod.response)

add(modules.impl.battle)

logs.append(["/crisis/getInfo", "crisis"])
logs.append(["/account/syncStatus", "syncStatus"])
logs.append(["/account/syncData", "syncData"])