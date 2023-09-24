import json


with open ("task2.json", 'r', encoding="utf-8") as f:
    data = json.load(f)

a = input("що потрібно?(name)")

for maki in data:
    print(maki)
