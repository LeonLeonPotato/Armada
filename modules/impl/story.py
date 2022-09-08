import mitmproxy.http
import json
import uuid

import util.utils as utils

def response(flow: mitmproxy.http.HTTPFlow):
    if(flow.request.path != "/account/syncData"): 
        return
    
    og = json.loads(flow.response.text)

    toReplace = { "init": 1 }
    stories = json.loads(utils.rf("cache/story_table.json"))
    for i, c in stories.items():
        toReplace[i] = 1
    og["user"]["status"]["flags"] = toReplace

    flow.response.set_text(json.dumps(og))

requests = []
responses = [response]