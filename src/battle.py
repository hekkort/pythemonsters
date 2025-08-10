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

    with open(os.path.join(monsters, "data", "csv", "types.csv"), mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            types = list(reader)

    for t in types:
        if t["identifier"] == move_type.value:
            move_type_id = t["id"]
    for type in target_type:
        for t in types:
            if t["identifier"] == type["identifier"]:
                target_type_id.append(t["id"])

    with open(os.path.join(monsters, "data", "csv", "type_efficacy.csv"), mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        type_efficacies = list(reader)
    for t_type_id in target_type_id:
        for t in type_efficacies:
            if t["target_type_id"] == t_type_id:
                if t["damage_type_id"] == move_type_id:
                    damage_factor = int(t["damage_factor"])
                    damage_factor *= 0.01
                    effectiveness *= damage_factor
    return effectiveness

def calculate_power(attacker: Pythemon, defender: Pythemon, action):
    action = int(action)
    if attacker.moves[action - 1]["damage_class"] == "physical":
        base_damage = (((((2 * attacker.level) / 5) + 2) * attacker.get_move_power(action) * (attacker.stats["attack"] / defender.stats["defense"])) / 50) + 2
    else:
        base_damage = (((((2 * attacker.level) / 5) + 2) * attacker.get_move_power(action) * (attacker.stats["special-attack"] / defender.stats["special-defense"])) / 50) + 2

    if attacker.moves[action - 1]["type_id"] in attacker.type:
        base_damage *= 1.5
    base_damage *= calculate_effectiveness(attacker, defender, action)
    base_damage *= random.uniform(0.85, 1)
    crit = random.random() < 0.0625
    if crit:
        return int(base_damage * 1.5), True
    return int(base_damage), False


def use_move(attacker: Pythemon, defender: Pythemon, action):
    if attacker.get_move_accuracy(action) == 1:
        return calculate_power(attacker, defender, action)
    miss = random.random()
    if miss > attacker.get_move_accuracy(action):
        return 0
    return calculate_power(attacker, defender, action)

def damage_to_your_pythemon(you: Pythemon, enemy: Pythemon):
    enemy_action = random.randint(1, 4)
    damage_to_you, crit = use_move(enemy, you, enemy_action)
    effectiveness_vs_you = calculate_effectiveness(enemy, you, enemy_action)
    you.health -= damage_to_you

    if damage_to_you != 0 and crit:
        if effectiveness_vs_you > 1:
            return f"The enemy {enemy.name} hit your {you.name} super effective and critically with {enemy.get_move_name(enemy_action)} for {damage_to_you}!"
        elif effectiveness_vs_you < 1:
            return f"The enemy {enemy.name} hit your {you.name} not very effective and critically with {enemy.get_move_name(enemy_action)} for {damage_to_you}!"
        else:
            return f"The enemy {enemy.name} hit your {you.name} critically with {enemy.get_move_name(enemy_action)} for {damage_to_you}!"
    elif damage_to_you != 0 and not crit:
        if effectiveness_vs_you > 1:
            return f"The enemy {enemy.name} hit your {you.name} super effective with {enemy.get_move_name(enemy_action)} for {damage_to_you}!"
        elif effectiveness_vs_you < 1:
            return f"The enemy {enemy.name} hit your {you.name} not very effective with {enemy.get_move_name(enemy_action)} for {damage_to_you}!"
        else:
            return f"The enemy {enemy.name} hit your {you.name} with {enemy.get_move_name(enemy_action)} for {damage_to_you}!"
    elif effectiveness_vs_you == 0:
        return f"The enemy's {enemy.name} {enemy.get_move_name(enemy_action)} doesn't affect {you.name}"
    else:
        return f"The enemy {enemy.name} used {enemy.get_move_name(enemy_action)}, but missed!"
    

def damage_to_enemy_pythemon(you: Pythemon, enemy: Pythemon, action):

    damage_to_enemy, crit = use_move(you, enemy, action)
    effectiveness_vs_enemy = calculate_effectiveness(you, enemy, action)
    enemy.health -= damage_to_enemy

    if damage_to_enemy != 0 and crit:
        if effectiveness_vs_enemy > 1:
            return f"Your {you.name} hit the enemy's {enemy.name} super effective and critically with {you.get_move_name(action)} for {damage_to_enemy}!"
        elif effectiveness_vs_enemy < 1:
            return f"Your {you.name} hit the enemy's {enemy.name} not very effective and critically with {you.get_move_name(action)} for {damage_to_enemy}!"
        else:
            return f"Your {you.name} hit the enemy's {enemy.name} critically with {you.get_move_name(action)} for {damage_to_enemy}!"
    elif damage_to_enemy != 0 and not crit:
        if effectiveness_vs_enemy > 1:
            return f"Your {you.name} hit the enemy's {enemy.name} super effective with {you.get_move_name(action)} for {damage_to_enemy}!"
        elif effectiveness_vs_enemy < 1:
            return f"Your {you.name} hit the enemy's {enemy.name} not very effective with {you.get_move_name(action)} for {damage_to_enemy}!"
        else:
            return f"Your {you.name} hit the enemy's {enemy.name} with {you.get_move_name(action)} for {damage_to_enemy}!"
    elif effectiveness_vs_enemy == 0:
        return f"Your {you.name}'s {you.get_move_name(action)} doesn't affect {you.name}"
    else:
        return f"Your {you.name} used {you.get_move_name(action)}, but missed!"

def dead(you: Pythemon, enemy: Pythemon):
    if you.health <= 0 or enemy.health <= 0:
        if enemy.health <= 0:
            return "You won!"
        else:
            return "The enemy won!"

def calculate_battle_logic(you: Pythemon, enemy: Pythemon, action):

    if you.stats["speed"] >= enemy.stats["speed"]:
        x = damage_to_enemy_pythemon(you, enemy, action)
        y = dead(you, enemy)
        if you.health <= 0 or enemy.health <= 0:
            return x, y

        a = damage_to_your_pythemon(you, enemy)
        b = dead(you, enemy)
        if you.health <= 0 or enemy.health <= 0:
            return a, b
        return x, a

    elif enemy.stats["speed"] > you.stats["speed"]:
        x = damage_to_your_pythemon(you, enemy)
        y = dead(you, enemy)
        if you.health <= 0 or enemy.health <= 0:
            return y, ""

        a = damage_to_enemy_pythemon(you, enemy, action)
        b = dead(you, enemy)
        if you.health <= 0 or enemy.health <= 0:
            return b, ""
        return x, a