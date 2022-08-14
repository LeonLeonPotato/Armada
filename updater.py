import os
from github import Github
import json

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

def pullCharData(force: bool):
    shouldUpdate = force or changeTime(char_table) == rf("cache/lastCharChanged.txt")
    if(shouldUpdate):
        cf("cache/char_table.json", requests.get(raw + char_table).text)

def pullModData(force: bool):
    shouldUpdate = force or changeTime(module_table) == rf("cache/lastModChanged.txt")
    if(shouldUpdate):
        cf("cache/mod_table.json", requests.get("https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/en_US/gamedata/excel/uniequip_table.json").text)

def run(force: bool):
    if(cfd("cache")):
        print("Creating Cache!")

    if(cfd("presets")):
        print("Creating Presets!")

    cf("cache/lastCharChanged.txt", changeTime(char_table))
    cf("cache/lastModChanged.txt", changeTime(module_table))

    pullModData(force)
    pullCharData(force)

if __name__ == "__main__":
    run(True)
    print("Patcher finished!")