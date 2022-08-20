import os
from github import Github

from utils import cf, cfd, rf

import requests

raw = "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/"

data_repo = "Kengxxiao/ArknightsGameData"
char_table = "en_US/gamedata/excel/character_table.json"
module_table = "en_US/gamedata/excel/uniequip_table.json"

generic_repo = "LeonLeonPotato/Armada-Rewrite"
generic_cc = "presets/generic_cc.json"

def changeTime(path: str) -> str: # stolen code ez
    commits = Github().get_repo(data_repo).get_commits(path=path)
    if commits.totalCount:
        return commits[0].commit.committer.date.strftime("%m/%d/%Y, %H:%M:%S")
    else:
        return "0"

def pullCharData(force: bool, shit = ""):
    shouldUpdate = force or (changeTime(char_table) if shit == "" else shit) == rf("cache/lastCharChanged.txt")
    if(shouldUpdate):
        cf("cache/char_table.json", requests.get(raw + char_table).text)

def pullModData(force: bool, shit = ""):
    shouldUpdate = force or (changeTime(module_table) if shit == "" else shit) == rf("cache/lastModChanged.txt")
    if(shouldUpdate):
        cf("cache/mod_table.json", requests.get(raw + module_table).text)

def run(force: bool):
    if(cfd("cache")):
        print("Creating Cache!")

    if(cfd("presets")):
        print("Creating Presets!")

    timeChar = changeTime(char_table)
    if(not os.path.exists("cache/lastCharChanged.txt")):
        cf("cache/lastCharChanged.txt", timeChar)
        pullCharData(True)
    else:
        pullCharData(force, timeChar)

    timeMod = changeTime(module_table)
    if(not os.path.exists("cache/lastModChanged.txt")):
        cf("cache/lastModChanged.txt", timeMod)
        pullModData(True)
    else:
        pullModData(force, timeMod)

if __name__ == "__main__":
    run(True)
    print("Patcher finished!")