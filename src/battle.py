import pythemon
import yaml
import os
import random

root_of_project = os.getcwd()
monsters = os.path.join(root_of_project + "/monsters/")

# # attacker = pythemon.Pythemon(random.randint(1, 151))
# # target = pythemon.Pythemon(random.randint(1, 151))
# attacker = pythemon.Pythemon
# action = random.randint(1, 4)

def calculate_effectiveness(attacker, target, action):
    move_type = attacker.get_move_type(action)
    target_type = target.type
    move_type_id = ""
    target_type_id = []
    effectiveness = 1

    with open(monsters + "data/types.yaml") as f:
        types = yaml.safe_load(f)
    for t in types:
        if t["identifier"] == move_type.value:
            move_type_id = t["id"]
    for type in target_type:
        for t in types:
            if t["identifier"] == type.value:
                target_type_id.append(t["id"])
    with open(monsters + "data/type_efficacy.yaml") as f:
        type_efficacies = yaml.safe_load(f)
    for t_type_id in target_type_id:
        for t in type_efficacies:
            if t["target_type_id"] == t_type_id:
                if t["damage_type_id"] == move_type_id:
                    damage_factor = int(t["damage_factor"])
                    damage_factor *= 0.01
                    effectiveness *= damage_factor
    return effectiveness
    
# effect = calculate_effectiveness(attacker, target, action)
# print(attacker.get_move_name(action))
# print(target.name)
# print(effect)
