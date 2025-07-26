import yaml
import os
from type import Type
import random

root_of_project = os.getcwd()
monsters = os.path.join(root_of_project + "/monsters/")
class Testing():
    def __init__(self, dex_entry):
        with open(monsters + "data/pokemon_species.yaml") as f:
            monster_species = yaml.safe_load(f)
        monster_species = monster_species[dex_entry - 1]
        self.dex_entry = monster_species["id"]
        self.name = monster_species["identifier"].capitalize()
        with open(monsters + "data/pokemon_types.yaml") as f:
            monster_types = yaml.safe_load(f)
        type_list = []
        for m in monster_types:
            if m["pokemon_id"] == f'{self.dex_entry}':
                type_list.append(m)
        with open(monsters + "data/types.yaml") as f:
            types = yaml.safe_load(f)
        self.type = []
        for i in range(len(type_list)):
            self.type.append(Type(types[int(type_list[i]["type_id"]) - 1]["identifier"]))
        with open(monsters + "data/moves.yaml") as f:
            moves = yaml.safe_load(f)

        self.moves = {}
        while len(self.moves) < 4:
            random_move = random.randint(1, 826)
            move = moves[random_move]

            if move["power"] != "":
                move_type = Type(types[int(move["type_id"]) - 1]["identifier"])

                if move_type in self.type:
                    name = move["identifier"].replace("-", " ").capitalize()
                    power = int(move["power"])
                    accuracy = float(move["accuracy"]) / 100
                    self.moves.update({(name, move_type): {power: accuracy}})

test = Testing(3)
print(test.dex_entry)
print(test.name)
print(test.type)
print(test.moves)