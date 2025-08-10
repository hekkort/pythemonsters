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

        # you = input("Select your pokemon by dex entry: ")
        # your_team[0] = pythemon.Pythemon(int(you))
        # enemy_team[0] = pythemon.Pythemon(random.randint(1, 151))
        your_team = []
        enemy_team = []

        for i in range(6):
            your_team.append(pythemon.Pythemon(random.randint(1, 151)))
            enemy_team.append(pythemon.Pythemon(random.randint(1, 151)))

        your_team_string = "Your team: "
        
        for i in range(len(your_team) - 1):
            your_team_string += your_team[i].name + ", "
        
        your_team_string += your_team[len(your_team) - 1].name

        enemy_team_string = "Enemy team: "
        
        for i in range(len(enemy_team) - 1):
            enemy_team_string += enemy_team[i].name + ", "
        
        enemy_team_string += enemy_team[len(enemy_team) - 1].name

        print(your_team_string)
        print(enemy_team_string)

        field = Field(your_team[0], enemy_team[0])
        drawn_field, dashes = field.draw_field()
        print(drawn_field)
        while True:
            
            action = input("What kind of attack do you want to use? Type just the number: ")

            drawn_field, dashes = field.draw_field()

            while not action.isdigit() or not (1 <= int(action) <= 4):
                action = input("Choose a valid integer, one through four: ")
                print("+" + dashes + "-" + dashes + "+")

            text_a, text_b = battle.calculate_battle_logic(your_team[0], enemy_team[0], action)
            drawn_field, dashes = field.draw_field()
            if your_team[0].health <= 0 or enemy_team[0].health <= 0:
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