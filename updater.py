import os
from github import Github
import util.utils as utils
import requests
import json

def changeTime(path: str) -> str: # stolen code ez
    commits = Github().get_repo("Kengxxiao/ArknightsGameData").get_commits(path=path)
    if commits.totalCount:
        return commits[0].commit.committer.date.strftime("%m/%d/%Y, %H:%M:%S")
    else:
        return "0"

def pull(force: bool, path : str, writeTo : str):
    localTime = json.loads(utils.rf("cache/changeTimes.json"))
    hubTime = changeTime(path)
    should = writeTo not in localTime or hubTime != localTime[writeTo] or force
    if(should):
        print("Pulling from " + path + " to " + writeTo + "!")
        utils.cf("cache/" + writeTo, requests.get("https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/" + path).text)
        localTime[writeTo] = hubTime
        utils.cf("cache/changeTimes.json", json.dumps(localTime))

def run(force: bool):
    if(utils.cfd("cache")):
        print("Creating cache!")

    if(utils.cfd("presets")):
        print("Creating presets!")

    if(utils.cfd("dump")):
        print("Creating dump!")

    if(not os.path.exists("cache/changeTimes.json")):
        utils.cf("cache/changeTimes.json", r"{}")

    pull(force, "en_US/gamedata/excel/character_table.json", "char_table.json")
    pull(force, "en_US/gamedata/excel/uniequip_table.json", "mod_table.json")
    pull(force, "en_US/gamedata/excel/stage_table.json", "stage_table.json")
    pull(force, "en_US/gamedata/excel/story_table.json", "story_table.json")


if __name__ == "__main__":
    run(True)
    print("Patcher finished!")