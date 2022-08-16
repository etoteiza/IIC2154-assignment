import json

def load_data():

    f = open("data.json", "r")
    data = []

    for line in f:
        data.append(json.loads(line))

    f.close()

    return data