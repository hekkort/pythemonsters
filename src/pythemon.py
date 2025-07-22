from type import Type

root = "/home/hekkort/workspace/github.com/hekkort/pythemonsters/monsters"

def make_ascii_of_monster(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return [line.rstrip("\n") for line in lines]

class Pythemon():
    def __init__(self, name):
        
        self.name = name.lower()
        match self.name:
            case "bulbasaur":
                self.type = [Type.GRASS, Type.POISON]
                self.moves = {"Vine Whip": {45: 1}, "Razor Leaf": {55: 0.95}, "Tackle": {40: 1}, "Poison Sting": {15: 1}}
            case "charmander":
                self.type = [Type.FIRE]
                self.moves = {"Ember": {40: 1}, "Tackle": {40: 1}, "Scratch": {40: 1}, "Fire Spin": {35: 0.85}}
            case "squirtle":
                self.type = [Type.WATER]
                self.moves = {"Water Gun": {40: 1}, "Rapid Spin": {50, 1}, "Bite": {60: 1}, "Whirlpool": {35: 0.85}}
        self.ascii_lines_back = make_ascii_of_monster(root + "/" + self.name + "_back.txt")
        self.ascii_lines_front = make_ascii_of_monster(root + "/" + self.name + "_front.txt")
        self.initial_health = 100