from field import *
import pythemon
import random
import make_yaml
import battle


def main():
    

    while True:

        make_yaml.make_yaml_from_csv()

        you = input("Select your pokemon by dex entry: ")
        your_pythemon = pythemon.Pythemon(int(you))
        enemy_pythemon = pythemon.Pythemon(random.randint(1, 151))
        

        field = Field(your_pythemon, enemy_pythemon)
        print(field.draw_field())
        while True:
            
            action = input("What kind of attack do you want to use? Type just the number: ")


            while not action.isdigit() or not (1 <= int(action) <= 4):
                action = input("Choose a valid integer, one through four: ")
                
            damage_to_enemy = your_pythemon.use_move(action)
            effectiveness_vs_enemy = battle.calculate_effectiveness(your_pythemon, enemy_pythemon, action)
            damage_to_enemy *= effectiveness_vs_enemy
            enemy_pythemon.health -= damage_to_enemy
            enemy_action = random.randint(1, 4)
            damage_to_you = enemy_pythemon.use_move(enemy_action)
            effectiveness_vs_you = battle.calculate_effectiveness(enemy_pythemon, your_pythemon, enemy_action)
            damage_to_you *= effectiveness_vs_you
            your_pythemon.health -= damage_to_you

            if your_pythemon.health <= 0 or enemy_pythemon.health <= 0:
                if enemy_pythemon.health <= 0:
                    print("You won!")
                else:
                    print("The enemy won!")
                break
            print(field.draw_field())



            if damage_to_enemy != 0:
                if effectiveness_vs_enemy > 1:
                    print(f"Your {your_pythemon.name} hit the enemy {enemy_pythemon.name} super effective with {your_pythemon.get_move_name(action)} for {damage_to_enemy}!")
                elif effectiveness_vs_enemy < 1:
                    print(f"Your {your_pythemon.name} hit the enemy {enemy_pythemon.name} not very effective with {your_pythemon.get_move_name(action)} for {damage_to_enemy}!")
                else:
                    print(f"Your {your_pythemon.name} hit the enemy {enemy_pythemon.name} with {your_pythemon.get_move_name(action)} for {damage_to_enemy}!")
            else:
                print(f"Your {your_pythemon.name} used {your_pythemon.get_move_name(action)}, but missed!")
            
            if damage_to_you != 0:
                if effectiveness_vs_you > 1:
                    print(f"The enemy {enemy_pythemon.name} hit your {your_pythemon.name} super effective with {enemy_pythemon.get_move_name(enemy_action)} for {damage_to_you}!")
                elif effectiveness_vs_you < 1:
                    print(f"The enemy {enemy_pythemon.name} hit your {your_pythemon.name} not very effective with {enemy_pythemon.get_move_name(enemy_action)} for {damage_to_you}!")
                else:
                    print(f"The enemy {enemy_pythemon.name} hit your {your_pythemon.name} with {enemy_pythemon.get_move_name(enemy_action)} for {damage_to_you}!")
            else:
                print(f"The enemy {enemy_pythemon.name} used {enemy_pythemon.get_move_name(enemy_action)}, but missed!")
        break




if __name__ == "__main__":
    main()
