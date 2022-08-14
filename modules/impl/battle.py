import mitmproxy.http
import json

def request(flow):
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