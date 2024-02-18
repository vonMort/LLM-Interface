
import json

def file_analysis(file_path):
    content = ""
    if ".py" in file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    elif ".json" in file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = json.dumps(json.load(file))
    return content