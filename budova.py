import json

data = {
    'name': 'John Doe',
    'age': 30,
    'occupation': 'Software Engineer'
}

with open ("data.json", 'w', encoding="utf-8") as f:
    json.dump(data, f, indent=4)