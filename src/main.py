from field import *
import pythemon
import random
import battle

chosen_pythemon = 0
choice = 0

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
        field = Field(your_team[chosen_pythemon], enemy_team[choice])
        drawn_field, dashes = field.draw_field()
        print(drawn_field)
        while all(y.health > 0 for y in your_team) and all(e.health > 0 for e in enemy_team):
            
            action = input("What kind of attack do you want to use? Type just the number: ")

            drawn_field, dashes = field.draw_field()

            while not action.isdigit() or not (1 <= int(action) <= 4):
                action = input("Choose a valid integer, one through four: ")
                print("+" + dashes + "-" + dashes + "+")

            text_a, text_b = battle.calculate_battle_logic(your_team[chosen_pythemon], enemy_team[choice], action)
            drawn_field, dashes = field.draw_field()

            you_dead(your_team, enemy_team, action, chosen_pythemon, choice, drawn_field, dashes)

            enemy_dead(your_team, enemy_team, action, chosen_pythemon, choice, drawn_field, dashes)


            print(drawn_field)
            print(text_a)
            print(text_b)
            print("+" + dashes + "-" + dashes + "+")

        break

def you_dead(your_team: list[Pythemon], enemy_team: list[Pythemon], action, chosen_pythemon, choice, drawn_field, dashes):
        if your_team[chosen_pythemon].health <= 0:
            print(drawn_field)
            print(text_a)
            print(text_b)
            print("+" + dashes + "-" + dashes + "+")
            name_of_alive = ""
            for element in your_team:
                if element.health > 0:
                    name_of_alive += f"{your_team.index(element)}. {element.name}, "

            chosen_pythemon = input("Choose a Pythemon: " + name_of_alive.strip()[:-1] + ": ")
            field = Field(your_team[int(chosen_pythemon)], enemy_team[choice])
            drawn_field, dashes = field.draw_field()
            print(drawn_field)
            action = input("What kind of attack do you want to use? Type just the number: ")

            drawn_field, dashes = field.draw_field()

            while not action.isdigit() or not (1 <= int(action) <= 4):
                action = input("Choose a valid integer, one through four: ")
                print("+" + dashes + "-" + dashes + "+")
            text_a, text_b = battle.calculate_battle_logic(your_team[int(chosen_pythemon)], enemy_team[choice], action)
            drawn_field, dashes = field.draw_field()
            print(drawn_field)
            print(text_a)
            print(text_b)
            print("+" + dashes + "-" + dashes + "+")
            if your_team[chosen_pythemon].health <= 0:
                you_dead(your_team, enemy_team, action, chosen_pythemon, choice, drawn_field, dashes)
            elif enemy_team[choice].health <= 0:
                enemy_dead(your_team, enemy_team, action, chosen_pythemon, choice, drawn_field, dashes)
            print(drawn_field)
            print(text_a)
            print(text_b)
            print("+" + dashes + "-" + dashes + "+")
        

def enemy_dead(your_team: list[Pythemon], enemy_team: list[Pythemon], action, chosen_pythemon, choice, drawn_field, dashes):
        if enemy_team[choice].health <= 0:
            print(drawn_field)
            print(text_a)
            print(text_b)
            print("+" + dashes + "-" + dashes + "+")
            name_of_alive = ""
            count = 1
            for element in enemy_team:
                if element.health > 0:
                    name_of_alive += f"{enemy_team.index(element)}. {element.name}, "
                    count += 1
            choice = random.randint(1, count)
            field = Field(your_team[chosen_pythemon], enemy_team[choice])
            drawn_field, dashes = field.draw_field()
            print(drawn_field)
            action = input("What kind of attack do you want to use? Type just the number: ")

            drawn_field, dashes = field.draw_field()

            while not action.isdigit() or not (1 <= int(action) <= 4):
                action = input("Choose a valid integer, one through four: ")
                print("+" + dashes + "-" + dashes + "+")
            text_a, text_b = battle.calculate_battle_logic(your_team[chosen_pythemon], enemy_team[choice], action)
            drawn_field, dashes = field.draw_field()
            print(drawn_field)
            print(text_a)
            print(text_b)
            print("+" + dashes + "-" + dashes + "+")
            if your_team[chosen_pythemon].health <= 0:
                you_dead(your_team, enemy_team, action, chosen_pythemon, choice, drawn_field, dashes)
            elif enemy_team[choice].health <= 0:
                enemy_dead(your_team, enemy_team, action, chosen_pythemon, choice, drawn_field, dashes)
            print(drawn_field)
            print(text_a)
            print(text_b)
            print("+" + dashes + "-" + dashes + "+")

if __name__ == "__main__":
    main()