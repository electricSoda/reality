import re
import json
import os

f = open(os.getcwd()+'\\tracked.json',)
categories = json.load(f)


def getType(processName: str, titleName: str) -> str:
    processName = processName.lower().replace(".exe", "")
    if processName not in categories:
        return "Other"
    
    titleName = titleName.lower()
    currApp = categories[processName]
    
    for key in list(currApp.keys()):
        if re.search(currApp[key], titleName):
            return key
        
def checkLimit(t: str, timeSpent: int) -> bool:
    if t in categories["-limits"]:
        if timeSpent > categories["-limits"][t]:
            return True
    return False

# Testing
if __name__ == "__main__":
    import time
    time.sleep(0.5)
    print(checkLimit("Entertainment", 3600))
    print(checkLimit("Entertainment", 3601))