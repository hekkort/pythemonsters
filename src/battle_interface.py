
def print_enemy_health(remaining_health, damage):
    if remaining_health - damage > 0:
        remaining_health -= damage
        return remaining_health

    else:
        return "Enemy has died!"

def print_me_health(remaining_health, damage):
    if remaining_health - damage > 0:
        remaining_health -= damage
        return remaining_health

    else:
        return "You have died!"

def print_battle_interface(damage_to_enemy, remaining_enemy, damage_to_me, remaining_me):
    print(f"""
====================
        {print_enemy_health(remaining_enemy, damage_to_enemy)}      


                                        {print_me_health(remaining_me, damage_to_me)}
                                ====================
----------------------------------------------------
|                                                  |
|                                                  |
|                                                  |
----------------------------------------------------
""")
    
    
