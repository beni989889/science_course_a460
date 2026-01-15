import os

os.getcwd

print(os.name)
print(os.cpu_count())
print(os.getlogin())

import json

data = {"name": "Emil", "age": 30}
s = json.dumps(data, sort_keys=True)
print(s)
print(json.loads(s)["name"])