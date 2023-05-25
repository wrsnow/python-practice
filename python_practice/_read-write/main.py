import os
import json
obj = {
    "author": "Mickey",
    "quote": "quote1"
}

json_cont = []

with open("json_test.json", "r") as f:
    file_cont = json.loads(f.read())
    if type(file_cont) == dict:
        json_cont.append(file_cont)
    else:
        json_cont = file_cont

print(json_cont)

with open("json_test.json", "w") as f:
    json_cont.append(obj)
    f.write(json.dumps(json_cont, indent=2))
