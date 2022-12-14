import mitmproxy.http
import json
import uuid

def battleStart(flow: mitmproxy.http.HTTPFlow):
    if(flow.request.path != "/quest/battleStart"): 
        return

    res = {
        "result": 0,
        "battleId": str(uuid.uuid1()),
        "apFailReturn": 0,
        "isApProtect": 0,
        "notifyPowerScoreNotEnoughIfFailed": False,
        "playerDataDelta": {
            "modified": {
                "status": {
                    "practiceTicket": 30
                }
            },
            "deleted": {}
        }
    }

    flow.response = mitmproxy.http.Response.make(
        200,
        json.dumps(res, indent=2).encode('utf-8')
    )

def battleEnd(flow: mitmproxy.http.HTTPFlow):
    if(flow.request.path != "/quest/battleFinish"):
        return

    res = {
        "result": 0,
        "playerDataDelta": {
            "modified": {},
            "deleted": {}
        }
    }

    flow.response = mitmproxy.http.Response.make(
        200,
        json.dumps(res, indent=2).encode('utf-8')
    )

def squad(flow: mitmproxy.http.HTTPFlow):
    if(flow.request.path != "/quest/squadFormation"):
        return

    req = json.loads(flow.request.text)

    res = {
        "playerDataDelta": {
            "deleted": {},
            "modified": {
                "troop": {
                    "squads": {
                        req["squadId"]: {
                            "slots": req["slots"]
                        }
                    }
                }
            }
        }
    }

    flow.response = mitmproxy.http.Response.make(
        200,
        json.dumps(res, indent=2).encode('utf-8')
    )

requests = [battleStart, battleEnd, squad]
responses = []