import webbrowser
import json


def browseropen(task):
    link = open("links.json", "r")
    obj = json.load(link)
    for i in obj["links"]:
        print(i)
        if i in task:
            print(i)
            webbrowser.open(obj["links"][i])
            return f"Opening {i}"