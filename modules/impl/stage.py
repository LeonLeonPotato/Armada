import mitmproxy.http
import json
import uuid

import util.utils as utils
import util.config as config

def response(flow: mitmproxy.http.HTTPFlow):
    if(flow.request.path != "/account/syncData"): 
        return

    data = json.loads(flow.response.text)
    stages = json.loads(utils.rf("cache/stage_table.json"))
    toReplace = {}
    for i, c in stages['stages'].items():
        stage = {
            "stageId": i,
            "completeTimes": 10,
            "startTimes": 10,
            "practiceTimes": 10,
            "state": 3,
            "hasBattleReplay": 1 if i in config.replays.keys() else 0,
            "noCostCnt": 0
        }
        toReplace[i] = stage

    data['user']['dungeon']['stages'] = toReplace

    flow.response.set_text(json.dumps(data))


requests = []
responses = [response]