from field import *
import pythemon
import random


def main():

    while True:

        you = input("Select your pokemon by dex entry: ")
        your_pythemon = pythemon.Pythemon(int(you))
        enemy_pythemon = pythemon.Pythemon(random.randint(1, 151))

        field = Field(your_pythemon, enemy_pythemon)
        print(field.draw_field())
        while True:
            
            action = input("What kind of attack do you want to use? Type just the number: ")


            while not action.isdigit() or not (1 <= int(action) <= 4):
                action = input("Choose a valid integer, one through four: ")
                

            
            enemy_pythemon.health -= your_pythemon.use_move(action)
            your_pythemon.health -= enemy_pythemon.use_move(random.randint(1, 4))

            if your_pythemon.health <= 0 or enemy_pythemon.health <= 0:
                break
            print(field.draw_field())
            if your_pythemon.use_move(action) != 0:
                print(f"You hit {enemy_pythemon.name} for {your_pythemon.use_move(action)}!")
            else:
                print(f"You missed!")
            
            if enemy_pythemon.use_move(action) != 0:
                print(f"Enemy hit {your_pythemon.name} for {enemy_pythemon.use_move(action)}!")
            else:
                print(f"Enemy missed!")
        break




if __name__ == "__main__":
    main()
