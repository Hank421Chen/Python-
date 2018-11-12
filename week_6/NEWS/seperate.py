import os
import json


def loadData(jsonpath):
    with open(jsonpath, 'r') as f:
        data = json.load(f)
    print(data)
    return data



currentPath = os.getcwd()
data = loadData(currentPath+"/run_results.json")

