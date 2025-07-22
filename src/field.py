from pythemon import *

class Field():
    def __init__(self, you, enemy):
        self.field_width = 100
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
    
    def add_enemy_health_padding(self):
        enemy_health_padding = ""
        for i in range(self.field_width // 2 - len(str(self.enemy.initial_health))):
            enemy_health_padding += " "
        return str(self.enemy.initial_health) + enemy_health_padding
    
    def add_you_health_padding(self):
        you_health_padding = ""
        for i in range(self.field_width // 2 - len(str(self.you.initial_health))):
            you_health_padding += " "
        return str(self.you.initial_health) + you_health_padding
    
    def format_moves_list(self, moves):
        for i in range(len(moves)):
            moves[i] = f" {i + 1}. {moves[i]}"
        return moves
    
    def format_ascii_right(self, spaces, index):
        return spaces[:-len(self.enemy.ascii_lines_front[index])] + self.enemy.ascii_lines_front[index]
    
    def format_ascii_left(self, spaces, index):
        return self.you.ascii_lines_back[index] + spaces[:-len(self.you.ascii_lines_back[index])]



    def draw_field(self):
        final_string = ""
        dashes = ""
        spaces = ""
        moves_list = self.format_moves_list(list(self.you.moves.keys()))

        for i in range(self.field_width // 2):
            dashes += "-"
            spaces += " "
        for i in range(len(moves_list)):
            padding = ""
            for j in range(len(spaces) - len(moves_list[i])):
                padding += " "
            moves_list[i] += padding
        for r in range(1):
            final_string += f"+{dashes}-{dashes}+\n"
            final_string += f"|{self.add_enemy_name_padding()} {self.format_ascii_right(spaces, 0)}|\n"
            final_string += f"|{self.add_enemy_health_padding()} {self.format_ascii_right(spaces, 1)}|\n"
            final_string += f"|{spaces} {self.format_ascii_right(spaces, 2)}|\n"
            for r in range(3, len(self.enemy.ascii_lines_front)):
                final_string += f"|{self.format_ascii_left(spaces, r - 3)} {self.format_ascii_right(spaces, r)}|\n"
            final_string += f"|{self.format_ascii_left(spaces, -3)} {spaces}|\n"
            final_string += f"|{self.format_ascii_left(spaces, -2)} {self.add_you_name_padding()}|\n"
            final_string += f"|{self.format_ascii_left(spaces, -1)} {self.add_you_health_padding()}|\n"
        final_string += f"+{dashes}" * 2 + "+\n"
        final_string += f"|{moves_list[0]}|{moves_list[1]}|\n"
        final_string += f"+{dashes}" * 2 + "+\n"
        final_string += f"|{moves_list[2]}|{moves_list[3]}|\n"
        final_string += f"+{dashes}" * 2 + "+\n"
        return final_string
    
   
