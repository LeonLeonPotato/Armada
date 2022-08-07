from cmath import phase
import subprocess
import sys
import uuid
import utils
import json
import armadapatcher
from character import Character

from colorama import Fore

import mitmproxy.ctx
import mitmproxy.http
import mitmproxy.flow
import mitmproxy.http

print(f"{Fore.MAGENTA}Armada rewrite by 3tnt{Fore.RESET}")
process = subprocess.run("adb devices", stdout=subprocess.PIPE)
emulators = process.stdout.decode("utf-8").count("emulator")
if(emulators >= 1):
    print(f"{Fore.YELLOW}[Warning] Multiple emulators found!{Fore.RESET}" , file=sys.stderr)
if(emulators < 1):
    print(f"{Fore.YELLOW}[Warning] No emulators found!{Fore.RESET}" , file=sys.stderr)

class Armada:
    def __init__(self):
        self.num = 0
        pass

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if(not utils.isAKServer(flow.request.host)): pass
        #print("Arknights connection outbound! " + flow.request.path)
        if(flow.request.path == "/quest/battleStart"):
            print("Battle started! Sending bullshit response")
            res = {
                "result": 0,
                "battleId": str(uuid.uuid1()),
                "apFailReturn": 5,
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

        if(flow.request.path == "/quest/battleFinish"):
            print("Battle finished! Sending bullshit response")
            res = {"result":0,"playerDataDelta":{"modified":{},"deleted":{}}}

            flow.response = mitmproxy.http.Response.make(
                200,
                json.dumps(res, indent=2).encode('utf-8')
            )
        

    # def response(self, flow: mitmproxy.http.HTTPFlow):
    #     if(flow.request.path == "/quest/battleStart"):
    #         armadapatcher.cfd("dump")
    #         armadapatcher.cf("dump/battleStartResponse.json", content=flow.response.text)

    #     if(flow.request.path == "/quest/battleFinish"):
    #         armadapatcher.cfd("dump")
    #         armadapatcher.cf("dump/battleFinishResponse.json", content=flow.response.text)
            #flow.response.set_text("{'result': 0, 'playerDataDelta': {'modified': {'status': {'practiceTicket': 100}}, 'deleted': {}}, 'data': ''}")

        # if(not utils.isAKServer(flow.request.host)): pass
        # pass

        # flow.response.status_code = 200

        # if(flow.request.path == "/story/finishStory"):
        #     print(flow.response.content.decode("utf-8"))

        # if(flow.request.path == "/charBuild/setEquipment"):
        #     f = open("output2.txt", "w")
        #     flow.response.set_text()
        #     f.close()

        # if(flow.request.path == "/account/syncData"):
        #     print("Syncing Data!")
        #     f = open("output.json", "r")
        #     flow.response.set_text(f.read())
        #     #f.write(flow.response.content.decode("utf-8"))
        #     f.close()



addons = [Armada()]