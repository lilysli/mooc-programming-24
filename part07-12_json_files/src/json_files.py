import json

def print_persons(filename: str):
    with open(filename, "r") as file:
        data = json.load(file)
        for person in data:
            print(f'{person["name"]} {person["age"]} years ({", ".join(person["hobbies"])})')

