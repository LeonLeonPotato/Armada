import mitmproxy.http
import json
import uuid

score = 0

# spite
def start(flow: mitmproxy.http.HTTPFlow):
    global score

    if(flow.request.path != "/crisis/battleStart"): 
        return

    res = json.loads(flow.request.text)
    for i in res["rune"]:
        if(i.find("buff") > -1):
            score = 0
            break
        score += int(i.split("_")[-1])

    toReturn = {
        "result": 0,
        "battleId": str(uuid.uuid1()),
        "playerDataDelta": {
            "deleted": {},
            "modified": {}
        },
        "sign": "7b1f67cd31d96a33702ca674b9a71f33ccb35cb3e74ea3dac20bb1d9f698a927a12cc25932ee4b4bea4570e01651f59935f3590d86cf0939ca7f56ee1a95d2f3fcdda9212c6c09e0b72289381f99eefac3fa598b2fdfd8d4a61a98a0f78b32e4ef3000414e268b6c04bedbe6b63d527bab3ce1a35d4a0f4c2894353142e31a1031822280849636d91c634f4b5e7380bb5ceab0203f95359ee1b09a102482348abf68f8a4df73f4e94972533582ae08ee3a012941d987c96b782a950a54851b501a823cdb7127b1fd260a40a7fc4c0bc254b5aaba5e7fa1791c5e0bb415ba36e3be4a39c38b955c07ad2c6bc6806f711bb17c966bbe519b48d70b4aeb86c7bddb",
        "signstr": "Fuck you hypergryph" # use frida
    }

    flow.response = mitmproxy.http.Response.make(
        200,
        json.dumps(toReturn, indent=2).encode('utf-8')
    )

def end(flow: mitmproxy.http.HTTPFlow):
    global score

    if(flow.request.path != "/crisis/battleFinish"): 
        return

    toReturn = {
        "result": 0,
        "playerDataDelta": {
            "deleted": {},
            "modified": {}
        },
        "score": score,
        "ts": 0,
        "updateInfo": {
            "point": {
                "after": score,
                "before": 0
            }
        }
    }

    flow.response = mitmproxy.http.Response.make(
        200,
        json.dumps(toReturn, indent=2).encode('utf-8')
    )

    score = 0

def info(flow: mitmproxy.http.HTTPFlow):
    if(flow.request.path != "/crisis/getInfo"): 
        return

    res = json.loads(flow.response.text)

    #res["playerDataDelta"]["modified"]["crisis"]["training"]["currentStage"] = ["tr_level_rune_04-01"]

    stages = res["data"]["trainingInfo"]["stages"].items()

    map_ = res["playerDataDelta"]["modified"]["crisis"]["map"]
    for i, c in stages:
        map_[i.replace("tr_level_", "")] = {
            "rank": 3,
            "confirmed": 3
        }

    training = res["playerDataDelta"]["modified"]["crisis"]["training"]["stage"]
    for i, c in stages:
        training[i] = { "point": 7 }

    season = res["playerDataDelta"]["modified"]["crisis"]["season"]["rune_season_8_1"]["permanent"]
    season["point"] = 38
    sex = season["rune"]
    for i, c in season["rune"].items():
        sex[i] =  1

    flow.response.set_text(json.dumps(res))


requests = [start, end]
responses = [info]