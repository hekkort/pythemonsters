from type import Type
from ascii_functions import *
import random
import ascii_magic
import os
import re
import yaml

root_of_project = os.getcwd()
monsters = os.path.join(root_of_project + "/monsters/")

class Pythemon():
    def __init__(self, dex_entry):

        with open(monsters + "data/pokemon_species.yaml") as f:
            monster_species = yaml.safe_load(f)
        monster_species = monster_species[dex_entry - 1]
        self.dex_entry = monster_species["id"]
        self.name = monster_species["identifier"].replace("-", " ").title()
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
        self.move_names = []
        while len(self.moves) < 4:
            random_move = random.randint(1, 826)
            move = moves[random_move - 1]

            if move["power"] != "" and move["accuracy"] != "":
                move_type = Type(types[int(move["type_id"]) - 1]["identifier"])

                if move_type in self.type or move_type == Type.NORMAL:
                    name_power_accuracy = move["identifier"].replace("-", " ").title() + f"    {move['power']} {move['accuracy']}"
                    name = move["identifier"].replace("-", " ").title()
                    power = int(move["power"])
                    accuracy = float(move["accuracy"]) / 100
                    self.moves.update({(name_power_accuracy, move_type): {power: accuracy}})
                    self.move_names.append(name)


        self._create_ascii_text_back(monsters)
        self._create_ascii_text_front(monsters)
        self.ascii_lines_back = make_ascii_of_monster_back(monsters + "text/back/" + str(self.dex_entry) + ".txt")
        self.ascii_lines_front = make_ascii_of_monster_front(monsters + "text/" + str(self.dex_entry) + ".txt")
        self.height_back = len(self.ascii_lines_back)
        self.height_front = len(self.ascii_lines_front)
        self.health = 400

    def _get_move_power(self, action):
        return list(self.moves[list(self.moves.keys())[int(action) - 1]].keys())[0]
    
    def _get_move_accuracy(self, action):
        outer_key = list(self.moves.keys())[int(action) - 1]
        inner_dict = self.moves[outer_key]
        inner_key = next(iter(inner_dict))
        return inner_dict[inner_key]
    
    def get_move_type(self, action):
        return list(self.moves.keys())[int(action) - 1][1]

    def get_move_name(self, action):
        return self.move_names[int(action) - 1]
    
    def use_move(self, action):
        if self._get_move_accuracy(action) == 1:
            return self._get_move_power(action)
        miss = random.random()
        if miss > self._get_move_accuracy(action):
            return 0
        return self._get_move_power(action)
    
    def _get_ascii_string(self, path):
        output = ascii_magic.from_image(path)
        ascii_colored = output.to_ascii(columns=60)
        ascii_grayscale = re.sub(r'\x1b\[[0-9;]*m', '', ascii_colored)
        return ascii_grayscale

    def _create_ascii_text_back(self, filepath):
        text = "text/"
        png = "png/"
        if os.path.isfile(filepath + text + f"back/{self.dex_entry}.txt"):
            with open(filepath + text + f"back/{self.dex_entry}.txt", "w", encoding="utf-8") as file:
                file.write(self._get_ascii_string(filepath + png + f"back/{self.dex_entry}.png"))
        else:
            os.makedirs(filepath + text + "back/", exist_ok=True)
            with open(filepath + text + f"back/{self.dex_entry}.txt", "w", encoding="utf-8") as file:
                file.write(self._get_ascii_string(filepath + png + f"back/{self.dex_entry}.png"))

    def _create_ascii_text_front(self, filepath):
        text = "text/"
        png = "png/"
        if os.path.isfile(filepath + text + f"{self.dex_entry}.txt"):
            with open(filepath + text + f"{self.dex_entry}.txt", "w", encoding="utf-8") as file:
                file.write(self._get_ascii_string(filepath + png + f"{self.dex_entry}.png"))

        else:
            os.makedirs(filepath + text, exist_ok=True)
            with open(filepath + text + f"{self.dex_entry}.txt", "w", encoding="utf-8") as file:
                file.write(self._get_ascii_string(filepath + png + f"{self.dex_entry}.png"))

    def print_front(self):
        for f in self.ascii_lines_front:
            print(f)
        
    def print_back(self):
        for b in self.ascii_lines_back:
            print(b)