import util.config as config
import util.utils as utils
import mitmproxy.http
import json

curBattleStage = None

def battle(flow: mitmproxy.http.HTTPFlow):
	global curBattleStage

	if(flow.request.path != "/quest/battleStart"): 
		return

	res = json.loads(flow.request.text)
	curBattleStage = res["stageId"]


def get_replay(flow: mitmproxy.http.HTTPFlow):
	if(flow.request.path != "/quest/getBattleReplay"): 
		return

	res = json.loads(flow.request.text)
	stage_id = res["stageId"]

	if(stage_id in config.replays):
		flow.response = mitmproxy.http.Response.make(
			200,
			json.dumps(config.replays[stage_id]).encode('utf-8')
		)

def set_replay(flow: mitmproxy.http.HTTPFlow):
	global curBattleStage

	if(flow.request.path != "/quest/saveBattleReplay"): 
		return

	res = json.loads(flow.request.text)
	stage_replay = res["battleReplay"]

	config.replays[curBattleStage] = stage_replay
	utils.cf("presets/" + config.replays_name, json.dumps(config.replays, indent=4))

	resp = {	
		"playerDataDelta": {
			"deleted": {},
			"modified": {
				"dungeon": {
					"stages": {
						curBattleStage: {
							"hasBattleReplay": 1
						}
					}
				}
			}
		},
		"result":0
	}

	flow.response = mitmproxy.http.Response.make(
		200,
		json.dumps(resp).encode('utf-8')
	)

requests = [get_replay, set_replay, battle]
responses = []