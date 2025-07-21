
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

def draw_field(moves):
    str = ""
    dashes = ""
    spaces = ""
    for i in range(24):
        dashes += "-"
        spaces += " "
    for i in range(len(moves)):
        padding = ""
        for j in range(len(spaces) - len(moves[i])):
            padding += " "
        moves[i] += padding
    for r in range(1):
        str += f"+{dashes}-{dashes}+\n"
        for r in range(12):
            str += f"|{spaces} {spaces}|\n"
    str += f"+{dashes}" * 2 + "+\n"
    str += f"|{moves[0]}|{moves[1]}|\n"
    str += f"+{dashes}" * 2 + "+\n"
    str += f"|{moves[2]}|{moves[3]}|\n"
    str += f"+{dashes}" * 2 + "+\n"
    return str
    
   
