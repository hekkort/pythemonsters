from field import *
import random
root_of_project = os.getcwd()
monsters = os.path.join(root_of_project, "monsters")

def calculate_effectiveness(attacker: Pythemon, target: Pythemon, action):
    move_type = attacker.get_move_type(action)
    target_type = target.type
    move_type_id = ""
    target_type_id = []
    effectiveness = 1

    with open(os.path.join(monsters, "data", "yaml", "types.yaml")) as f:
        types = yaml.safe_load(f)
    for t in types:
        if t["identifier"] == move_type.value:
            move_type_id = t["id"]
    for type in target_type:
        for t in types:
            if t["identifier"] == type["identifier"]:
                target_type_id.append(t["id"])
    with open(os.path.join(monsters, "data", "yaml", "type_efficacy.yaml")) as f:
        type_efficacies = yaml.safe_load(f)
    for t_type_id in target_type_id:
        for t in type_efficacies:
            if t["target_type_id"] == t_type_id:
                if t["damage_type_id"] == move_type_id:
                    damage_factor = int(t["damage_factor"])
                    damage_factor *= 0.01
                    effectiveness *= damage_factor
    return effectiveness

def damage_to_your_pythemon(you: Pythemon, enemy: Pythemon, action):
    enemy_action = random.randint(1, 4)
    damage_to_you_float = enemy.use_move(enemy_action)
    damage_to_you = int(damage_to_you_float)
    effectiveness_vs_you = calculate_effectiveness(enemy, you, enemy_action)
    damage_to_you *= effectiveness_vs_you
    you.health -= damage_to_you

    if damage_to_you != 0:
        if effectiveness_vs_you > 1:
            print(f"The enemy {enemy.name} hit your {you.name} super effective with {enemy.get_move_name(enemy_action)} for {damage_to_you}!")
        elif effectiveness_vs_you < 1:
            print(f"The enemy {enemy.name} hit your {you.name} not very effective with {enemy.get_move_name(enemy_action)} for {damage_to_you}!")
        elif effectiveness_vs_you == 0:
            print(f"Your {enemy.name}'s {enemy.get_move_name(action)} doesn't affect {you.name}")
        else:
            print(f"The enemy {enemy.name} hit your {you.name} with {enemy.get_move_name(enemy_action)} for {damage_to_you}!")
    else:
        print(f"The enemy {enemy.name} used {enemy.get_move_name(enemy_action)}, but missed!")

def damage_to_enemy_pythemon(you: Pythemon, enemy: Pythemon, action):
    damage_to_enemy_float = you.use_move(action)
    damage_to_enemy = int(damage_to_enemy_float)
    effectiveness_vs_enemy = calculate_effectiveness(you, enemy, action)
    damage_to_enemy *= effectiveness_vs_enemy
    enemy.health -= damage_to_enemy

    if damage_to_enemy != 0:
        if effectiveness_vs_enemy > 1:
            print(f"Your {you.name} hit the enemy {enemy.name} super effective with {you.get_move_name(action)} for {damage_to_enemy}!")
        elif effectiveness_vs_enemy < 1:
            print(f"Your {you.name} hit the enemy {enemy.name} not very effective with {you.get_move_name(action)} for {damage_to_enemy}!")
        elif effectiveness_vs_enemy == 0:
            print(f"Your {you.name}'s {you.get_move_name(action)} doesn't affect {enemy.name}")
        else:
            print(f"Your {you.name} hit the enemy {enemy.name} with {you.get_move_name(action)} for {damage_to_enemy}!")
    else:
        print(f"Your {you.name} used {you.get_move_name(action)}, but missed!")

def calculate_battle_logic(you: Pythemon, enemy: Pythemon, action):
    

    if you.stats["speed"] >= enemy.stats["speed"]:
        damage_to_enemy_pythemon(you, enemy, action)

        if you.health <= 0 or enemy.health <= 0:
            if enemy.health <= 0:
                print("You won!")
                return
            else:
                print("The enemy won!")
                return
        damage_to_your_pythemon(you, enemy, action)

        if you.health <= 0 or enemy.health <= 0:
            if enemy.health <= 0:
                print("You won!")
                return
            else:
                print("The enemy won!")
                return
        return

    elif enemy.stats["speed"] > you.stats["speed"]:
        damage_to_your_pythemon(you, enemy, action)
        
        if you.health <= 0 or enemy.health <= 0:
            if enemy.health <= 0:
                print("You won!")
                return
            else:
                print("The enemy won!")
                return
        damage_to_enemy_pythemon(you, enemy, action)

        if you.health <= 0 or enemy.health <= 0:
            if enemy.health <= 0:
                print("You won!")
                return
            else:
                print("The enemy won!")
                return
        return
    
def damage_to_your_pythemon(you: Pythemon, enemy: Pythemon, action):
    enemy_action = random.randint(1, 4)
    damage_to_you_float = enemy.use_move(enemy_action)
    damage_to_you = int(damage_to_you_float)
    effectiveness_vs_you = calculate_effectiveness(enemy, you, enemy_action)
    damage_to_you *= effectiveness_vs_you
    you.health -= damage_to_you

    if damage_to_you != 0:
        if effectiveness_vs_you > 1:
            print(f"The enemy {enemy.name} hit your {you.name} super effective with {enemy.get_move_name(enemy_action)} for {damage_to_you}!")
        elif effectiveness_vs_you < 1:
            print(f"The enemy {enemy.name} hit your {you.name} not very effective with {enemy.get_move_name(enemy_action)} for {damage_to_you}!")
        elif effectiveness_vs_you == 0:
            print(f"Your {enemy.name}'s {enemy.get_move_name(action)} doesn't affect {you.name}")
        else:
            print(f"The enemy {enemy.name} hit your {you.name} with {enemy.get_move_name(enemy_action)} for {damage_to_you}!")
    else:
        print(f"The enemy {enemy.name} used {enemy.get_move_name(enemy_action)}, but missed!")