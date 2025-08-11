from field import *
import pythemon
import random
import battle


def main():

    chosen_pythemon = 0
    choice = 0
    all_choices = []
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
        field = Field(your_team[chosen_pythemon], enemy_team[choice])
        drawn_field, dashes = field.draw_field()
        print(drawn_field)
        
        while any(y.health > 0 for y in your_team) and any(e.health > 0 for e in enemy_team):

            action = input("What kind of attack do you want to use? Type just the number: ")

            while not action.isdigit() or not (1 <= int(action) <= 4):
                action = input("Choose a valid integer, one through four: ")
                print("+" + dashes + "-" + dashes + "+")

            text_a, text_x, text_b = battle.calculate_battle_logic(your_team[chosen_pythemon], enemy_team[choice], action)
            field = Field(your_team[chosen_pythemon], enemy_team[choice])
            drawn_field, dashes = field.draw_field()

            if your_team[chosen_pythemon].health <= 0:
                chosen_pythemon = you_dead(your_team, chosen_pythemon, drawn_field, dashes, text_a, text_x, text_b)
            elif enemy_team[choice].health <= 0:
                choice, all_choices = enemy_dead(your_team, enemy_team, chosen_pythemon, choice, drawn_field, dashes, text_a, text_x, text_b, all_choices)
            else:
                print(drawn_field)
                print(text_a)
                print(text_x)
                print(text_b)
                print("+" + dashes + "-" + dashes + "+")
        break


def you_dead(your_team: list[Pythemon], chosen_pythemon, drawn_field, dashes, text_a, text_x, text_b):
        if your_team[chosen_pythemon].health <= 0:
            print(drawn_field)
            print(text_a)
            print(text_x)
            print(text_b)
            print("+" + dashes + "-" + dashes + "+")
            name_of_alive = ""
            for element in your_team:
                if element.health > 0:
                    name_of_alive += f"{your_team.index(element)}. {element.name}, "

            chosen_pythemon = input("Choose a Pythemon: " + name_of_alive.strip()[:-1] + ": ")

            return int(chosen_pythemon)

            # drawn_field, dashes = field.draw_field()
            # print(drawn_field)
            # action = input("What kind of attack do you want to use? Type just the number: ")

            # drawn_field, dashes = field.draw_field()

            # while not action.isdigit() or not (1 <= int(action) <= 4):
            #     action = input("Choose a valid integer, one through four: ")
            #     print("+" + dashes + "-" + dashes + "+")
            # text_a, text_b = battle.calculate_battle_logic(your_team[int(chosen_pythemon)], enemy_team[choice], action)
            # drawn_field, dashes = field.draw_field()
            # print(drawn_field)
            # print(text_a)
            # print(text_b)
            # print("+" + dashes + "-" + dashes + "+")
            # if your_team[chosen_pythemon].health <= 0:
            #     you_dead(your_team, enemy_team, action, chosen_pythemon, choice, drawn_field, dashes)
            # elif enemy_team[choice].health <= 0:
            #     enemy_dead(your_team, enemy_team, action, chosen_pythemon, choice, drawn_field, dashes)
            # print(drawn_field)
            # print(text_a)
            # print(text_b)
            # print("+" + dashes + "-" + dashes + "+")
        

def enemy_dead(your_team: list[Pythemon], enemy_team: list[Pythemon], chosen_pythemon, choice, drawn_field, dashes, text_a, text_x, text_b, all_choices: list):
        if enemy_team[choice].health <= 0:
            print(drawn_field)
            print(text_a)
            print(text_x)
            print(text_b)
            print("+" + dashes + "-" + dashes + "+")
            name_of_alive = ""
            for element in enemy_team:
                if element.health > 0:
                    name_of_alive += f"{enemy_team.index(element)}. {element.name}, "
            choice = random.randint(1, len(enemy_team) - 1)
            all_choices.append(choice)
            while choice in all_choices:
                choice = random.randint(1, len(enemy_team) - 1)
            field = Field(your_team[chosen_pythemon], enemy_team[choice])
            drawn_field, dashes = field.draw_field()
            print(drawn_field)
            return choice, all_choices
            # field = Field(your_team[chosen_pythemon], enemy_team[choice])
            # drawn_field, dashes = field.draw_field()
            # print(drawn_field)
            # action = input("What kind of attack do you want to use? Type just the number: ")

            # drawn_field, dashes = field.draw_field()

            # while not action.isdigit() or not (1 <= int(action) <= 4):
            #     action = input("Choose a valid integer, one through four: ")
            #     print("+" + dashes + "-" + dashes + "+")
            # text_a, text_b = battle.calculate_battle_logic(your_team[chosen_pythemon], enemy_team[choice], action)
            # drawn_field, dashes = field.draw_field()
            # print(drawn_field)
            # print(text_a)
            # print(text_b)
            # print("+" + dashes + "-" + dashes + "+")
            # if your_team[chosen_pythemon].health <= 0:
            #     you_dead(your_team, enemy_team, action, chosen_pythemon, choice, drawn_field, dashes)
            # elif enemy_team[choice].health <= 0:
            #     enemy_dead(your_team, enemy_team, action, chosen_pythemon, choice, drawn_field, dashes)
            # print(drawn_field)
            # print(text_a)
            # print(text_b)
            # print("+" + dashes + "-" + dashes + "+")

if __name__ == "__main__":
    main()