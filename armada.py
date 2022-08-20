import utils
import updater
import modules.manager
import atexit

from colorama import Fore

import mitmproxy.ctx
import mitmproxy.http
import mitmproxy.flow

print(f"{Fore.MAGENTA}Armada rewrite by 3tnt{Fore.RESET}")
# process = subprocess.run("adb devices", stdout=subprocess.PIPE)
# emulators = process.stdout.decode("utf-8").count("emulator")
# if(emulators >= 1):
#     print(f"{Fore.YELLOW}[Warning] Multiple emulators found!{Fore.RESET}" , file=sys.stderr)
# if(emulators < 1):
#     print(f"{Fore.YELLOW}[Warning] No emulators found!{Fore.RESET}" , file=sys.stderr)

#updater.run(False)
print("Updater finished!")

def exit_handler():
    import pathlib; 
    [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]
    [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]

atexit.register(exit_handler)

class Armada:
    def __init__(self):
        pass

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if(not utils.isAKServer(flow.request.host)): pass

        for fun in modules.manager.requests:
            fun(flow)

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if(not utils.isAKServer(flow.request.host)): pass
        
        for fun in modules.manager.responses:
            fun(flow)

        for log in modules.manager.logs:
            if(flow.request.path == log[0]):
                utils.cf("dump/" + log[1] + "Response.json", flow.response.text)
                utils.cf("dump/" + log[1] + "Request.json", flow.request.text)
addons = [Armada()]