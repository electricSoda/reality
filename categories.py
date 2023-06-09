import re
import json
import os

f = open(os.getcwd()+'\\\\tracked.json',)
categories = json.load(f)


def getType(processName: str, titleName: str):
    processName = processName.lower().replace(".exe", "")
    if processName not in categories:
        return "Other"
    
    titleName = titleName.lower()
    currApp = categories[processName]
    
    for key in list(currApp.keys()):
        if re.search(currApp[key], titleName):
            return key
