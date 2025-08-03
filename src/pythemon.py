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

        with open(monsters + "data/yaml/pokemon_species.yaml") as f:
            monster_species = yaml.safe_load(f)
        monster_species = monster_species[dex_entry - 1]
        
        self.dex_entry = int(monster_species["id"])
        self.name = monster_species["identifier"].replace("-", " ").title()
        self.type = self._set_types()
        self.moves = self._set_moves()
        self.level = 100
        self.iv = self._set_iv()
        self.ev = self._set_ev()
        self.base_stats = self._set_base_stats()
        self.health = self._set_hp_at_level()
        self.stats = self._set_max_stats()

        self._create_ascii_text_back(monsters)
        self._create_ascii_text_front(monsters)
        self.ascii_lines_back = make_ascii_of_monster_back(monsters + "text/back/" + str(self.dex_entry) + ".txt")
        self.ascii_lines_front = make_ascii_of_monster_front(monsters + "text/" + str(self.dex_entry) + ".txt")
        self.height_back = len(self.ascii_lines_back)
        self.height_front = len(self.ascii_lines_front)

    def _set_moves(self):
        with open(monsters + "data/yaml/moves.yaml") as f:
            moves = yaml.safe_load(f)
        moves_of_type = []
        for m in moves:
            for t in self.type:
                if m["type_id"] == t["type_id"]:
                    m.update({"type": t["identifier"]})
                    moves_of_type.append(m)
        move_set = []
        while len(move_set) < 4:
            random_move = random.randint(1, len(moves_of_type))
            move = moves_of_type[random_move - 1]
            if move["power"] != "" and move["accuracy"] != "":
                move_set.append(move)
        return move_set

    def _set_types(self):
        with open(monsters + "data/yaml/pokemon_types.yaml") as f:
            monster_types = yaml.safe_load(f)
        type_list = []
        for m in monster_types:
            if m["pokemon_id"] == f'{self.dex_entry}':
                type_list.append(m)
        with open(monsters + "data/yaml/types.yaml") as f:
            types = yaml.safe_load(f)
        for t in type_list:
            for item in types:
                if t["type_id"] == item["id"]:
                    t.update({"identifier": item["identifier"]})
        return type_list
    
    def _set_hp_at_level(self):
        hp = ((2 * int(self.base_stats[0]["base_stat"]) + self.iv[0] + (self.ev[0] // 4)) * self.level // 100) + self.level + 10
        print(f"For {self.name} adding: {hp} for hp")
        return hp
    
    def _set_max_stats(self):
        stats = {}
        stats.update({"hp": self.health})
        
        for i in range(5):
            identifier = self.base_stats[i + 1]["identifier"]
            stat = (((2 * int(self.base_stats[i + 1]['base_stat']) + self.iv[i + 1] + (self.ev[i + 1] // 4)) * self.level) // 100) + 5
            stats.update({identifier: stat})
            print(f"For {self.name} adding: {stat} for {identifier}")
        return stats

    def _set_iv(self):
        iv = []
        for i in range(6):
            iv.append(random.randint(0, 31))
        return iv
    
    def _set_ev(self):
        ev = []
        for i in range(6):
            ev.append(0)
        return ev

    def _set_base_stats(self):
        with open(monsters + "data/yaml/stats.yaml") as f:
            stats = yaml.safe_load(f)
        with open(monsters + "data/yaml/pokemon_stats.yaml") as f:
            pokemon_stats = yaml.safe_load(f)
        pokemon_stat_list = []
        for p in pokemon_stats:
            if p["pokemon_id"] == str(self.dex_entry):
                pokemon_stat_list.append(p)
        for i in range(len(pokemon_stat_list)):
            pokemon_stat_list[i].update({"identifier": stats[i]["identifier"]})
        return pokemon_stat_list

    def _get_move_power(self, action):
        return int(self.moves[int(action) - 1]["power"])
    
    def _get_move_accuracy(self, action):
        return int(self.moves[int(action) - 1]["accuracy"])
    
    def get_move_type(self, action):
        return Type(self.moves[int(action) - 1]["type"])

    def get_move_name(self, action):
        return self.moves[int(action) - 1]["identifier"].title()
    
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
