from type import Type
from ascii_functions import *
import random
import ascii_magic
import os
import re
import csv

root_of_project = os.getcwd()
monsters = os.path.join(root_of_project, "monsters")
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

class Pythemon():
    def __init__(self, dex_entry):
        with open(os.path.join(monsters, "data", "csv", "pokemon_species.csv"), mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            monster_species = list(reader)

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
        self.ascii_lines_back = make_ascii_of_monster_back(os.path.join(monsters, "text", "back", f"{self.dex_entry}.txt"))
        self.ascii_lines_front = make_ascii_of_monster_front(os.path.join(monsters, "text", f"{self.dex_entry}.txt"))
        self.height_back = len(self.ascii_lines_back)
        self.height_front = len(self.ascii_lines_front)
    
    def _set_moves(self):
        with open(os.path.join(monsters, "data", "csv", "pokemon_moves.csv"), mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            pokemon_moves = list(reader)
        moves_of_pythemon = []
        for d in pokemon_moves:
            if d["pokemon_id"] == str(self.dex_entry):
                moves_of_pythemon.append(d)

        with open(os.path.join(monsters, "data", "csv", "moves.csv"), mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            moves = list(reader)
        all_moves_set = []
        with open(os.path.join(monsters, "data", "csv", "types.csv"), mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            types = list(reader)
        for m in moves_of_pythemon:
            for item in moves:
                if m["move_id"] == item["id"]:
                    for t in types:
                        if t["id"] == item["type_id"]:
                            item.update({"type": t["identifier"]})
                    all_moves_set.append(item)
        move_set = []
        while len(move_set) < 4:
            random_move = random.randint(1, len(all_moves_set))
            move = all_moves_set[random_move - 1]
            if move["power"] != "" and move["accuracy"] != "":
                if move not in move_set:
                    move_set.append(move)
        return move_set

    def _set_types(self):
        with open(os.path.join(monsters, "data", "csv", "pokemon_types.csv"), mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            monster_types = list(reader)
        type_list = []
        for m in monster_types:
            if m["pokemon_id"] == f'{self.dex_entry}':
                type_list.append(m)
        with open(os.path.join(monsters, "data", "csv", "types.csv"), mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            types = list(reader)
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
        with open(os.path.join(monsters, "data", "csv", "stats.csv"), mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            stats = list(reader)
        with open(os.path.join(monsters, "data", "csv", "pokemon_stats.csv"), mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            pokemon_stats = list(reader)

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
        back = os.path.join(filepath, "text", "back", f"{self.dex_entry}.txt")
        back_png = os.path.join(filepath, "png", "back", f"{self.dex_entry}.png")
        if os.path.isfile(back):
            with open(back, "w", encoding="utf-8") as file:
                file.write(self._get_ascii_string(back_png))
        else:
            os.makedirs(os.path.join(filepath, "text", "back"), exist_ok=True)
            with open(back, "w", encoding="utf-8") as file:
                file.write(self._get_ascii_string(back_png))

    def _create_ascii_text_front(self, filepath):
        front = os.path.join(filepath, "text", f"{self.dex_entry}.txt")
        front_png = os.path.join(filepath, "png", f"{self.dex_entry}.png")
        if os.path.isfile(front):
            with open(front, "w", encoding="utf-8") as file:
                file.write(self._get_ascii_string(front_png))

        else:
            os.makedirs(os.path.join(filepath, "text"), exist_ok=True)
            with open(front, "w", encoding="utf-8") as file:
                file.write(self._get_ascii_string(front_png))

    def print_front(self):
        for f in self.ascii_lines_front:
            print(f)
        
    def print_back(self):
        for b in self.ascii_lines_back:
            print(b)
