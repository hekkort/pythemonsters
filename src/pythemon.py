from type import Type
from ascii_functions import *
import random
import ascii_magic
import os
import re

monsters = "/home/hekkort/workspace/github.com/hekkort/pythemonsters/monsters/"

class Pythemon():
    def __init__(self, name):
        
        self.name = name.capitalize()
        match self.name:
            case "Bulbasaur":
                self.type = [Type.GRASS, Type.POISON]
                self.moves = {"Vine Whip": {45: 1}, "Razor Leaf": {55: 0.95}, "Tackle": {40: 1}, "Poison Sting": {15: 1}}
                self.dex_entry = 1
            case "Charmander":
                self.type = [Type.FIRE]
                self.moves = {"Ember": {40: 1}, "Tackle": {40: 1}, "Scratch": {40: 1}, "Fire Spin": {35: 0.85}}
                self.dex_entry = 4
            case "Squirtle":
                self.type = [Type.WATER]
                self.moves = {"Water Gun": {40: 1}, "Rapid Spin": {50, 1}, "Bite": {60: 1}, "Whirlpool": {35: 0.85}}
                self.dex_entry = 7
        self._create_ascii_text_back(monsters)
        self._create_ascii_text_front(monsters)
        self.ascii_lines_back = make_ascii_of_monster_back(monsters + "text/back/" + self.name.lower() + "_back.txt")
        self.ascii_lines_front = make_ascii_of_monster_front(monsters + "text/" + self.name.lower() + "_front.txt")
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
    
    def _get_ascii_string(self, path):
        output = ascii_magic.from_image(path)
        ascii_colored = output.to_ascii()
        ascii_grayscale = re.sub(r'\x1b\[[0-9;]*m', '', ascii_colored)
        return ascii_grayscale

    def _create_ascii_text_back(self, filepath):
        back = "_back.txt"
        text = "text/"
        png = "png/"
        if os.path.isfile(filepath + text + "back/" + self.name.lower() + back):
            os.remove(filepath + text + "back/" + self.name.lower() + back)
        with open(filepath + text + "back/" + self.name.lower() + back, "w", encoding="utf-8") as file:
            file.write(self._get_ascii_string(filepath + png + f"back/{self.dex_entry}.png"))

    def _create_ascii_text_front(self, filepath):
        back = "_front.txt"
        text = "text/"
        png = "png/"
        if os.path.isfile(filepath + text + self.name.lower() + back):
            os.remove(filepath + text + self.name.lower() + back)
        with open(filepath + text + self.name.lower() + back, "w", encoding="utf-8") as file:
            file.write(self._get_ascii_string(filepath + png + f"{self.dex_entry}.png"))










