import csv
import yaml
import os

root_of_project = os.getcwd()
monsters = os.path.join(root_of_project + "/monsters/" + "data/")
def make_yaml_from_csv():
    if not os.path.exists(monsters + "moves.yaml"):
        with open(monsters + "moves.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            moves = list(reader)

        with open(monsters + "moves.yaml", "w", encoding="utf-8") as f:
            yaml.dump(moves, f, allow_unicode=True)

    if not os.path.exists(monsters + "pokemon_species.yaml"):
        with open(monsters + "pokemon_species.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            moves = list(reader)

        with open(monsters + "pokemon_species.yaml", "w", encoding="utf-8") as f:
            yaml.dump(moves, f, allow_unicode=True)

    if not os.path.exists(monsters + "types.yaml"):
        with open(monsters + "types.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            moves = list(reader)

        with open(monsters + "types.yaml", "w", encoding="utf-8") as f:
            yaml.dump(moves, f, allow_unicode=True)

    if not os.path.exists(monsters + "pokemon_types.yaml"):
        with open(monsters + "pokemon_types.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            moves = list(reader)

        with open(monsters + "pokemon_types.yaml", "w", encoding="utf-8") as f:
            yaml.dump(moves, f, allow_unicode=True)

    if not os.path.exists(monsters + "type_efficacy.yaml"):
        with open(monsters + "type_efficacy.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            moves = list(reader)

        with open(monsters + "type_efficacy.yaml", "w", encoding="utf-8") as f:
            yaml.dump(moves, f, allow_unicode=True)