import json

def open_operations_json():
    with open("operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data

