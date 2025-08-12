from field import *
import pythemon
import random
import battle


def main():

    chosen_pythemon = 0
    choice = 0

    while True:
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
                chosen_pythemon = you_dead(your_team, enemy_team, choice, chosen_pythemon, drawn_field, dashes, text_a, text_x, text_b)
            elif enemy_team[choice].health <= 0:
                choice = enemy_dead(your_team, enemy_team, chosen_pythemon, choice, drawn_field, dashes, text_a, text_x, text_b)
            else:
                print(drawn_field)
                print(text_a)
                print(text_x)
                print(text_b)
                print("+" + dashes + "-" + dashes + "+")
        break


def you_dead(your_team: list[Pythemon], enemy_team: list[Pythemon], choice, chosen_pythemon, drawn_field, dashes, text_a, text_x, text_b):
    choice = int(choice)
    chosen_pythemon = int(chosen_pythemon)
    valid_choices = []
    for y in your_team:
        if y.health > 0:
            valid_choices.append(your_team.index(y))
    print(drawn_field)
    print(text_a)
    print(text_x)
    print(text_b)
    print("+" + dashes + "-" + dashes + "+")
    name_of_alive = ""
    for element in your_team:
        if element.health > 0:
            name_of_alive += f"{your_team.index(element)}. {element.name}, "
    if valid_choices:
        chosen_pythemon = input("Choose a Pythemon: " + name_of_alive.strip()[:-1] + ": ")
        print("+" + dashes + "-" + dashes + "+")
        while not chosen_pythemon.isdigit() or int(chosen_pythemon) not in valid_choices:
            chosen_pythemon = input(f"Choose a valid integer: {name_of_alive.strip()[:-1]}: ")
            print("+" + dashes + "-" + dashes + "+")
        chosen_pythemon = int(chosen_pythemon)
        field = Field(your_team[chosen_pythemon], enemy_team[choice])
        drawn_field, dashes = field.draw_field()
        print(drawn_field)
    else:
        field = Field(your_team[chosen_pythemon], enemy_team[choice])
        drawn_field, dashes = field.draw_field()
        print(drawn_field)
        print(f"The enemy won and had {name_of_alive.strip()[:-1]} left!")
        print("+" + dashes + "-" + dashes + "+")
        return
    return chosen_pythemon
        

def enemy_dead(your_team: list[Pythemon], enemy_team: list[Pythemon], chosen_pythemon, choice, drawn_field, dashes, text_a, text_x, text_b):
    chosen_pythemon = int(chosen_pythemon)
    choice = int(choice)
    valid_choices = []
    for e in enemy_team:
        if e.health > 0:
            valid_choices.append(enemy_team.index(e))
    print(drawn_field)
    print(text_a)
    print(text_x)
    print(text_b)
    print("+" + dashes + "-" + dashes + "+")
    name_of_alive = ""
    for element in enemy_team:
        if element.health > 0:
            name_of_alive += f"{enemy_team.index(element)}. {element.name}, "
    print(f"Enemy still has: {name_of_alive.strip()[:-1]}")
    if valid_choices:
        choice = random.choice(valid_choices)
        field = Field(your_team[chosen_pythemon], enemy_team[choice])
        drawn_field, dashes = field.draw_field()
        print(drawn_field)
    else:
        field = Field(your_team[chosen_pythemon], enemy_team[choice])
        drawn_field, dashes = field.draw_field()
        print(drawn_field)
        print(f"You won and you had {name_of_alive.strip()[:-1]} left!")
        print("+" + dashes + "-" + dashes + "+")
        return
    return choice

if __name__ == "__main__":
    main()