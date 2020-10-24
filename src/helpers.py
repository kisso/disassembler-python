import json


def load_file(path: str):
    with open(file=path) as f:
        return f.read().splitlines()


def load_json(path: str):
    with open(file=path) as json_file:
        return json.load(json_file)
