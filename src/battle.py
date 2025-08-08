from field import *
import pythemon
import random
import make_yaml

root_of_project = os.getcwd()
monsters = os.path.join(root_of_project, "monsters")

# # attacker = pythemon.Pythemon(random.randint(1, 151))
# # target = pythemon.Pythemon(random.randint(1, 151))
# attacker = pythemon.Pythemon
# action = random.randint(1, 4)

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

# def calculate_battle_logic(you: Pythemon, enemy: Pythemon, action):

#     if you.stats["speed"] > enemy.stats["speed"]:
#         damage_to_enemy = you.use_move(action)
#         effectiveness_vs_enemy = calculate_effectiveness(you, enemy, action)
#         damage_to_enemy *= effectiveness_vs_enemy
#         enemy.health -= damage_to_enemy
#         if you.health <= 0 or enemy.health <= 0:
#             if enemy.health <= 0:
#                 print("You won!")
#                 return
#             else:
#                 print("The enemy won!")
#                 return

#         enemy_action = random.randint(1, 4)
#         damage_to_you = enemy.use_move(enemy_action)
#         effectiveness_vs_you = calculate_effectiveness(enemy, you, enemy_action)
#         damage_to_you *= effectiveness_vs_you
#         you.health -= damage_to_you

#     elif enemy.stats["speed"] > you.stats["speed"]:
#         enemy_action = random.randint(1, 4)
#         damage_to_you = enemy.use_move(enemy_action)
#         effectiveness_vs_you = calculate_effectiveness(enemy, you, enemy_action)
#         damage_to_you *= effectiveness_vs_you
#         you.health -= damage_to_you

#         damage_to_enemy = you.use_move(action)
#         effectiveness_vs_enemy = calculate_effectiveness(you, enemy, action)
#         damage_to_enemy *= effectiveness_vs_enemy
#         enemy.health -= damage_to_enemy

    
# effect = calculate_effectiveness(attacker, target, action)
# print(attacker.get_move_name(action))
# print(target.name)
# print(effect)
