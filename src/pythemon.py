from type import Type
from ascii_functions import *
import random
import ascii_magic
import os
import re
from PIL import Image

monsters = "/home/hekkort/workspace/github.com/hekkort/pythemonsters/monsters/"

class Pythemon():
    def __init__(self, dex_entry):
        
        self.dex_entry = dex_entry
        match self.dex_entry:
            case 1:
                self.type = [Type.GRASS, Type.POISON]
                self.moves = {"Vine Whip": {45: 1}, "Razor Leaf": {55: 0.95}, "Tackle": {40: 1}, "Poison Sting": {15: 1}}
                self.name = "Bulbasaur"
            case 4:
                self.type = [Type.FIRE]
                self.moves = {"Ember": {40: 1}, "Tackle": {40: 1}, "Scratch": {40: 1}, "Fire Spin": {35: 0.85}}
                self.name = "Charmander"
            case 7:
                self.type = [Type.WATER]
                self.moves = {"Water Gun": {40: 1}, "Rapid Spin": {50, 1}, "Bite": {60: 1}, "Whirlpool": {35: 0.85}}
                self.name = "Squirtle"
            case 150:
                self.type = [Type.PSYCHIC]
                self.moves = {"Psybeam": {65: 1}, "Brick Break": {75, 1}, "Psyshock": {80: 1}, "Psychic": {90: 1}}
                self.name = "Mewtwo"
            case _:
                self.type = [Type.NORMAL]
                self.moves = {"Move 1": {10: 1}, "Move 2": {10, 1}, "Move 3": {10: 1}, "Move 4": {10: 1}}
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
        
        miss = random.random()
        if miss > self._get_move_accuracy(action):
            return 0
        return self._get_move_power(action)
    
    def _resize_src_img(self):
        img = Image.open(f"{self.dex_entry}.png")
        img.thumbnail((10, 10))  # Max width and height
        img.save(f"{self.dex_entry}.jpg")
    
    def _get_ascii_string(self, path):
        self._resize_src_img()
        output = ascii_magic.from_image(path)
        ascii_colored = output.to_ascii()
        ascii_grayscale = re.sub(r'\x1b\[[0-9;]*m', '', ascii_colored)
        return ascii_grayscale

    def _create_ascii_text_back(self, filepath):
        text = "text/"
        png = "png/"
        if os.path.isfile(filepath + text + f"back/{self.dex_entry}.txt"):
            os.remove(filepath + text + f"back/{self.dex_entry}.txt")
        if not os.path.isdir(filepath + text + "back/"):
            os.mkdir(filepath + text)
            os.mkdir(filepath + text + "back/")
        with open(filepath + text + f"back/{self.dex_entry}.txt", "w", encoding="utf-8") as file:
            file.write(self._get_ascii_string(filepath + png + f"back/{self.dex_entry}.png"))

    def _create_ascii_text_front(self, filepath):
        text = "text/"
        png = "png/"
        if os.path.isfile(filepath + text + f"{self.dex_entry}.txt"):
            os.remove(filepath + text + f"{self.dex_entry}.txt")
        if not os.path.isdir(filepath + text):
            os.mkdir(filepath + text)
        with open(filepath + text + f"{self.dex_entry}.txt", "w", encoding="utf-8") as file:
            file.write(self._get_ascii_string(filepath + png + f"{self.dex_entry}.png"))

    def print_front(self):
        for f in self.ascii_lines_front:
            print(f)
        
    def print_back(self):
        for b in self.ascii_lines_back:
            print(b)