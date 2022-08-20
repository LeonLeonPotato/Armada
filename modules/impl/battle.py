import mitmproxy.http
import json
import uuid

def request(flow: mitmproxy.http.HTTPFlow):
    res = {}

    if(flow.request.path == "/quest/battleStart"): 
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
    elif(flow.request.path == "/quest/battleFinish"): 
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
    

def response(flow: mitmproxy.http.HTTPFlow):
    pass