from src.battle_interface import *


def main():
    moves = [" 1. flamethrower", " 2. sandattack", " 3. mud-slap", " 4. earthquake"]
    print(draw_field(48, moves, "fronk", "harry"))
    


if __name__ == "__main__":
    main()
