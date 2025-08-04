import csv
import yaml
import os

root_of_project = os.getcwd()
monsters = os.path.join(root_of_project, "monsters", "data")
def make_yaml_from_csv():
    moves_yaml = os.path.join(monsters, "yaml", "moves.yaml")
    moves_csv = os.path.join(monsters, "csv", "moves.csv")

    if not os.path.exists(moves_yaml):
        with open(os.path.join(moves_csv), encoding="utf-8") as f:
            reader = csv.DictReader(f)
            moves = list(reader)

        with open(moves_yaml, "w", encoding="utf-8") as f:
            yaml.dump(moves, f, allow_unicode=True)

    
    pokemon_species_yaml = os.path.join(monsters, "yaml", "pokemon_species.yaml")
    pokemon_species_csv = os.path.join(monsters, "csv", "pokemon_species.csv")

    if not os.path.exists(pokemon_species_yaml):
        with open(pokemon_species_csv, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            pokemon_species = list(reader)

        with open(pokemon_species_yaml, "w", encoding="utf-8") as f:
            yaml.dump(pokemon_species, f, allow_unicode=True)
    
    types_yaml = os.path.join(monsters, "yaml", "types.yaml")
    types_csv = os.path.join(monsters, "csv", "types.csv")

    if not os.path.exists(types_yaml):
        with open(types_csv, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            types = list(reader)

        with open(types_yaml, "w", encoding="utf-8") as f:
            yaml.dump(types, f, allow_unicode=True)

    pokemon_types_yaml = os.path.join(monsters, "yaml", "pokemon_types.yaml")
    pokemon_types_csv = os.path.join(monsters, "csv", "pokemon_types.csv")

    if not os.path.exists(pokemon_types_yaml):
        with open(pokemon_types_csv, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            pokemon_types = list(reader)

        with open(pokemon_types_yaml, "w", encoding="utf-8") as f:
            yaml.dump(pokemon_types, f, allow_unicode=True)
    
    type_efficacy_yaml = os.path.join(monsters, "yaml", "type_efficacy.yaml")
    type_efficacy_csv = os.path.join(monsters, "csv", "type_efficacy.csv")

    if not os.path.exists(type_efficacy_yaml):
        with open(type_efficacy_csv, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            type_efficacy = list(reader)

        with open(type_efficacy_yaml, "w", encoding="utf-8") as f:
            yaml.dump(type_efficacy, f, allow_unicode=True)

    pokemon_stats_yaml = os.path.join(monsters, "yaml", "pokemon_stats.yaml")
    pokemon_stats_csv = os.path.join(monsters, "csv", "pokemon_stats.csv")

    if not os.path.exists(pokemon_stats_yaml):
        with open(pokemon_stats_csv, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            pokemon_stats = list(reader)

        with open(pokemon_stats_yaml, "w", encoding="utf-8") as f:
            yaml.dump(pokemon_stats, f, allow_unicode=True)
    
    stats_yaml = os.path.join(monsters, "yaml", "stats.yaml")
    stats_csv = os.path.join(monsters, "csv", "stats.csv")
    
    if not os.path.exists(stats_yaml):
        with open(stats_csv, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            stats = list(reader)

        with open(stats_yaml, "w", encoding="utf-8") as f:
            yaml.dump(stats, f, allow_unicode=True)

