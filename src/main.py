from field import *
import pythemon
import random
import battle


def main():
    

    while True:

        battle.make_yaml_from_csv()

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
            enemy_action = random.randint(1, 4)
            your_pythemon.health -= enemy_pythemon.use_move(enemy_action)

            if your_pythemon.health <= 0 or enemy_pythemon.health <= 0:
                if enemy_pythemon.health <= 0:
                    print("You won!")
                else:
                    print("The enemy won!")
                break
            print(field.draw_field())
            if your_pythemon.use_move(action) != 0:
                print(f"Your {your_pythemon.name} hit the enemy {enemy_pythemon.name} with {your_pythemon.get_move_name(action)} for {your_pythemon.use_move(action)}!")
            else:
                print(f"You missed!")
            
            if enemy_pythemon.use_move(action) != 0:
                print(f"The enemy {enemy_pythemon.name} hit your {your_pythemon.name} with {enemy_pythemon.get_move_name(enemy_action)} for {enemy_pythemon.use_move(enemy_action)}!")
            else:
                print(f"Enemy missed!")
        break




if __name__ == "__main__":
    main()
