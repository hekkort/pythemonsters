import csv
import yaml
import os

root_of_project = os.getcwd()
monsters = os.path.join(root_of_project + "/monsters/" + "data/")
def make_yaml_from_csv():
    if not os.path.exists(monsters + "yaml/moves.yaml"):
        with open(monsters + "csv/moves.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            moves = list(reader)

        with open(monsters + "yaml/moves.yaml", "w", encoding="utf-8") as f:
            yaml.dump(moves, f, allow_unicode=True)

    if not os.path.exists(monsters + "yaml/pokemon_species.yaml"):
        with open(monsters + "csv/pokemon_species.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            pokemon_species = list(reader)

        with open(monsters + "yaml/pokemon_species.yaml", "w", encoding="utf-8") as f:
            yaml.dump(pokemon_species, f, allow_unicode=True)

    if not os.path.exists(monsters + "yaml/types.yaml"):
        with open(monsters + "csv/types.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            types = list(reader)

        with open(monsters + "yaml/types.yaml", "w", encoding="utf-8") as f:
            yaml.dump(types, f, allow_unicode=True)

    if not os.path.exists(monsters + "yaml/pokemon_types.yaml"):
        with open(monsters + "csv/pokemon_types.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            pokemon_types = list(reader)

        with open(monsters + "yaml/pokemon_types.yaml", "w", encoding="utf-8") as f:
            yaml.dump(pokemon_types, f, allow_unicode=True)

    if not os.path.exists(monsters + "yaml/type_efficacy.yaml"):
        with open(monsters + "csv/type_efficacy.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            type_efficacy = list(reader)

        with open(monsters + "yaml/type_efficacy.yaml", "w", encoding="utf-8") as f:
            yaml.dump(type_efficacy, f, allow_unicode=True)

    if not os.path.exists(monsters + "yaml/pokemon_stats.yaml"):
        with open(monsters + "csv/pokemon_stats.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            pokemon_stats = list(reader)

        with open(monsters + "yaml/pokemon_stats.yaml", "w", encoding="utf-8") as f:
            yaml.dump(pokemon_stats, f, allow_unicode=True)
    
    if not os.path.exists(monsters + "yaml/stats.yaml"):
        with open(monsters + "csv/stats.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            stats = list(reader)

        with open(monsters + "yaml/stats.yaml", "w", encoding="utf-8") as f:
            yaml.dump(stats, f, allow_unicode=True)

