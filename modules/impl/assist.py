import mitmproxy.http
import json
import time
import math

lastRequests = {
    "PIONEER": None,
    "WARRIOR": None,
    "TANK": None,
    "SNIPER": None,
    "CASTER": None,
    "MEDIC": None,
    "SUPPORT": None,
    "SPECIAL": None
}

curProfession = None
bypass = False

def request(flow: mitmproxy.http.HTTPFlow):
    global lastRequests
    global curProfession
    global bypass


    if(flow.request.path != "/quest/getAssistList"): 
        return

    res = json.loads(flow.request.text)
    curProfession = res["profession"]
    lastRequest = lastRequests[curProfession]

    if(lastRequest != None and not res["askRefresh"]):
        bypass = True
        flow.response = mitmproxy.http.Response.make(
            200,
            json.dumps(lastRequest).encode('utf-8')
        )

def response(flow: mitmproxy.http.HTTPFlow):
    global lastRequests
    global curProfession
    global bypass

    if(flow.request.path != "/quest/getAssistList"):
        return

    if(bypass):
        bypass = False
        return

    res = json.loads(flow.response.text)

    for i in res["assistList"]:
        i["isFriend"] = True
        i["canRequestFriend"] = False

    lastRequests[curProfession] = res

    flow.response.set_text(json.dumps(res))

requests = [request]
responses = [response]
