import json

with open ("data.json", 'r', ) as f:
    data = json.load(f)

data['age'] = 16
data['name'] = 'Vladyslav Utrata'
data['occupation'] = 'SBU '

with open ("data.json", 'w', ) as f:
    json.dump(data, f, indent=4)

