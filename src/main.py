from field import *
import pythemon
import random
import battle


def main():


    while True:

        you = input("Select your pokemon by dex entry: ")
        your_pythemon = pythemon.Pythemon(int(you))
        enemy_pythemon = pythemon.Pythemon(random.randint(1, 151))
        

        field = Field(your_pythemon, enemy_pythemon)
        drawn_field, dashes = field.draw_field()
        print(drawn_field)
        while True:
            
            action = input("What kind of attack do you want to use? Type just the number: ")

            drawn_field, dashes = field.draw_field()
            print("+" + dashes + "-" + dashes + "+")

            while not action.isdigit() or not (1 <= int(action) <= 4):
                action = input("Choose a valid integer, one through four: ")
                print("+" + dashes + "-" + dashes + "+")

            battle.calculate_battle_logic(your_pythemon, enemy_pythemon, action)
            if your_pythemon.health <= 0 or enemy_pythemon.health <= 0:
                break
            drawn_field, dashes = field.draw_field()
            print(drawn_field)

        break




if __name__ == "__main__":
    main()
