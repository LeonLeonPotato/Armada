import mitmproxy.http
import json
import uuid

import util.config as config

def response(flow: mitmproxy.http.HTTPFlow):
    if(flow.request.path != "/account/syncData"): 
        return
    
    og = json.loads(flow.response.text)
    status = og["user"]["status"]

    status["nickName"] = config.name
    status["level"] = config.level
    status["exp"] = config.exp
    status["payDiamond"] = 0 # f2p moment
    status["freeDiamond"] = config.primes
    status["diamondShard"] = config.orundums
    status["gold"] = config.lmd
    # status["uid"] = config.uid # lost code due to pc reset, will implement later (lazy + cc8)
    status["secretary"] = config.assistant
    status["secretarySkinId"] = config.assistant + "#" + str(config.skin)

    flow.response.set_text(json.dumps(og))

requests = []
responses = [response]