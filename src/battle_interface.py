
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

def draw_field(field_width, moves, enemy_name, your_name):
    final_string = ""
    dashes = ""
    spaces = ""
    enemy_health = 0
    your_health = 0
    enemy_name_padding = ""
    your_name_padding = ""
    enemy_health_padding = ""
    your_health_padding = ""

    for i in range(field_width // 2 - len(enemy_name)):
        enemy_name_padding += " "
    for i in range(field_width // 2 - len(your_name)):
        your_name_padding += " "

    for i in range(field_width // 2 - len(str(enemy_health))):
        enemy_health_padding += " "
    for i in range(field_width // 2 - len(str(your_health))):
        your_health_padding += " "
    for i in range(field_width // 2):
        dashes += "-"
        spaces += " "
    for i in range(len(moves)):
        padding = ""
        for j in range(len(spaces) - len(moves[i])):
            padding += " "
        moves[i] += padding
    for r in range(1):
        final_string += f"+{dashes}-{dashes}+\n"
        final_string += f"|{enemy_name}{enemy_name_padding} {spaces}|\n"
        final_string += f"|{enemy_health}{enemy_health_padding} {spaces}|\n"
        for r in range(8):
            final_string += f"|{spaces} {spaces}|\n"
        final_string += f"|{spaces} {your_name}{your_name_padding}|\n"
        final_string += f"|{spaces} {your_health}{your_health_padding}|\n"
    final_string += f"+{dashes}" * 2 + "+\n"
    final_string += f"|{moves[0]}|{moves[1]}|\n"
    final_string += f"+{dashes}" * 2 + "+\n"
    final_string += f"|{moves[2]}|{moves[3]}|\n"
    final_string += f"+{dashes}" * 2 + "+\n"
    return final_string
    
   
