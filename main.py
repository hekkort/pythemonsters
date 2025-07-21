from src.battle_interface import *
import sys

def main():
    damage_to_enemy = sys.argv[1]
    damage_to_me = sys.argv[2]
    print_battle_interface(int(damage_to_enemy),
                            400, int(damage_to_me), 300)


if __name__ == "__main__":
    main()
