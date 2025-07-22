from type import Type
from ascii_functions import *

monsters = "/home/hekkort/workspace/github.com/hekkort/pythemonsters/monsters"

class Pythemon():
    def __init__(self, name):
        
        self.name = name.capitalize()
        match self.name:
            case "Bulbasaur":
                self.type = [Type.GRASS, Type.POISON]
                self.moves = {"Vine Whip": {45: 1}, "Razor Leaf": {55: 0.95}, "Tackle": {40: 1}, "Poison Sting": {15: 1}}
            case "Charmander":
                self.type = [Type.FIRE]
                self.moves = {"Ember": {40: 1}, "Tackle": {40: 1}, "Scratch": {40: 1}, "Fire Spin": {35: 0.85}}
            case "Squirtle":
                self.type = [Type.WATER]
                self.moves = {"Water Gun": {40: 1}, "Rapid Spin": {50, 1}, "Bite": {60: 1}, "Whirlpool": {35: 0.85}}
        self.ascii_lines_back = make_ascii_of_monster_back(monsters + "/" + self.name.lower() + "_back.txt")
        self.ascii_lines_front = make_ascii_of_monster_front(monsters + "/" + self.name.lower() + "_front.txt")
        self.health = 100