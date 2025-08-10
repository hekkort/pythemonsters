from field import *
import pythemon
import random
import battle


def main():
    # your_team = []
    # enemy_team = []

    # for i in range(6):
    #     your_team.append(pythemon.Pythemon(random.randint(1, 151)))
    #     enemy_team.append(pythemon.Pythemon(random.randint(1, 151)))
    
    # print("My team:")
    # for i in range(6):
    #     print(your_team[i])
    # print("Enemy team:")
    # for i in range(6):
    #     print(enemy_team[i])

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

            while not action.isdigit() or not (1 <= int(action) <= 4):
                action = input("Choose a valid integer, one through four: ")
                print("+" + dashes + "-" + dashes + "+")

            text_a, text_b = battle.calculate_battle_logic(your_pythemon, enemy_pythemon, action)
            drawn_field, dashes = field.draw_field()
            if your_pythemon.health <= 0 or enemy_pythemon.health <= 0:
                print(drawn_field)
                print(text_a)
                print(text_b)
                print("+" + dashes + "-" + dashes + "+")
                break
            print(drawn_field)
            print(text_a)
            print(text_b)
            print("+" + dashes + "-" + dashes + "+")

        break




if __name__ == "__main__":
    main()
