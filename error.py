import re, json

with open("logs.json","r") as file:
    data = json.load(file)
    print(data[0])