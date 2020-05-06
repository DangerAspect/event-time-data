import json

data = None

with open("data/legacy.json") as f:
    data = json.load(f)

for key, value in data.items():
    filename = key + ".json"
    filename = filename.replace("/", "-")

    print(f"Saving {filename}")
    with open(f"data/{filename}", "w") as f:
        json.dump(data[key], f, indent=4)


