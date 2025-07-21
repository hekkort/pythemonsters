from src.battle_interface import *


def main():
    moves = {" 1. flamethrower": 120, " 2. sandattack": 0, " 3. mud-slap": 40, " 4. earthquake": 100}
    print(draw_field(48, moves, "jan wouter verbeek", "robby stofbergen"))
    


if __name__ == "__main__":
    main()
