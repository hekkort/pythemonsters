from pythemon import *

class Field():
    def __init__(self, field_width, you, enemy):
        self.field_width = field_width
        self.you = you
        self.enemy = enemy

    def add_enemy_name_padding(self):
        enemy_name_padding = ""
        for i in range(self.field_width // 2 - len(self.enemy.name)):
            enemy_name_padding += " "
        return self.enemy.name + enemy_name_padding
    
    def add_you_name_padding(self):
        you_name_padding = ""
        for i in range(self.field_width // 2 - len(self.you.name)):
            you_name_padding += " "
        return self.you.name + you_name_padding


    def draw_field():
        final_string = ""
        
        
        
        # final_string = ""
        # dashes = ""
        # spaces = ""
        # enemy_name_padding = ""
        # your_name_padding = ""
        # enemy_health_padding = ""
        # your_health_padding = ""
        # moves_list = list(moves.keys())

        # for i in range(field_width // 2 - len(enemy_name)):
        #     enemy_name_padding += " "
        # for i in range(field_width // 2 - len(your_name)):
        #     your_name_padding += " "

        # for i in range(field_width // 2 - len(str(insert_enemy_health()))):
        #     enemy_health_padding += " "
        # for i in range(field_width // 2 - len(str(insert_your_health()))):
        #     your_health_padding += " "
        # for i in range(field_width // 2):
        #     dashes += "-"
        #     spaces += " "
        # for i in range(len(moves)):
        #     padding = ""
        #     for j in range(len(spaces) - len(moves_list[i])):
        #         padding += " "
        #     moves_list[i] += padding
        # for r in range(1):
        #     final_string += f"+{dashes}-{dashes}+\n"
        #     final_string += f"|{enemy_name}{enemy_name_padding} {spaces}|\n"
        #     final_string += f"|{insert_enemy_health()}{enemy_health_padding} {spaces}|\n"
        #     for r in range(16):
        #         final_string += f"|{spaces} {spaces}|\n"
        #     final_string += f"|{spaces} {your_name}{your_name_padding}|\n"
        #     final_string += f"|{spaces} {insert_your_health()}{your_health_padding}|\n"
        # final_string += f"+{dashes}" * 2 + "+\n"
        # final_string += f"|{moves_list[0]}|{moves_list[1]}|\n"
        # final_string += f"+{dashes}" * 2 + "+\n"
        # final_string += f"|{moves_list[2]}|{moves_list[3]}|\n"
        # final_string += f"+{dashes}" * 2 + "+\n"
        # return final_string
    
   
