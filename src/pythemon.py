from type import Type
from ascii_functions import *
import random
import ascii_magic
import os
import re
from PIL import Image

root_of_project = os.getcwd()
monsters = os.path.join(root_of_project + "/monsters/")
class Pythemon():
    def __init__(self, dex_entry):
        
        self.dex_entry = dex_entry
        match self.dex_entry:
            case 1:
                self.type = [Type.GRASS, Type.POISON]
                self.moves = {("Vine Whip", Type.GRASS): {45: 1}, ("Razor Leaf", Type.GRASS): {55: 0.95}, ("Tackle", Type.NORMAL): {40: 1}, ("Poison Sting", Type.POISON): {15: 1}}
                self.name = "Bulbasaur"
            case 4:
                self.type = [Type.FIRE]
                self.moves = {("Ember", Type.FIRE): {40: 1}, ("Tackle", Type.NORMAL): {40: 1}, ("Scratch", Type.NORMAL): {40: 1}, ("Fire Spin", Type.NORMAL): {35: 0.85}}
                self.name = "Charmander"
            case 7:
                self.type = [Type.WATER]
                self.moves = {("Water Gun", Type.WATER): {40: 1}, ("Rapid Spin", Type.NORMAL): {50: 1}, ("Bite", Type.DARK): {60: 1}, ("Whirlpool", Type.WATER): {35: 0.85}}
                self.name = "Squirtle"
            case 150:
                self.type = [Type.PSYCHIC]
                self.moves = {("Psybeam", Type.PSYCHIC): {65: 1}, ("Brick Break", Type.FIGHTING): {75: 1}, ("Psyshock", Type.PSYCHIC): {80: 1}, ("Psychic", type.PSYCHIC): {90: 1}}
                self.name = "Mewtwo"
            case _:
                self.type = [Type.NORMAL]
                self.moves = {("Move 1", Type.NORMAL): {10: 1}, ("Move 2", Type.NORMAL): {10: 1}, ("Move 3", Type.NORMAL): {10: 1}, ("Move 4", Type.NORMAL): {10: 1}}
                self.name = "Placeholder"
        self._create_ascii_text_back(monsters)
        self._create_ascii_text_front(monsters)
        self.ascii_lines_back = make_ascii_of_monster_back(monsters + "text/back/" + str(self.dex_entry) + ".txt")
        self.ascii_lines_front = make_ascii_of_monster_front(monsters + "text/" + str(self.dex_entry) + ".txt")
        self.height_back = len(self.ascii_lines_back)
        self.height_front = len(self.ascii_lines_front)
        self.health = 100

    def _get_move_power(self, action):
        
        return list(self.moves[list(self.moves.keys())[int(action) - 1]].keys())[0]
    
    def _get_move_accuracy(self, action):

        outer_key = list(self.moves.keys())[int(action) - 1]
        inner_dict = self.moves[outer_key]
        inner_key = next(iter(inner_dict))
        return inner_dict[inner_key]
    
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