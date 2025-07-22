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
        return enemy_name_padding + self.enemy.name
    
    def add_you_name_padding(self):
        you_name_padding = ""
        for i in range(self.field_width // 2 - len(self.you.name)):
            you_name_padding += " "
        return self.you.name + you_name_padding
    
    def add_enemy_health_padding(self):
        enemy_health_padding = ""
        for i in range(self.field_width // 2 - len(str(self.enemy.health))):
            enemy_health_padding += " "
        return enemy_health_padding + str(self.enemy.health)
    
    def add_you_health_padding(self):
        you_health_padding = ""
        for i in range(self.field_width // 2 - len(str(self.you.health))):
            you_health_padding += " "
        return str(self.you.health) + you_health_padding
    
    def format_moves_list(self, moves):
        for i in range(len(moves)):
            moves[i] = f" {i + 1}. {moves[i]}"
        return moves
    
    def format_ascii_right(self, spaces, index):
        return spaces[:-len(self.enemy.ascii_lines_front[index])] + self.enemy.ascii_lines_front[index]
    
    def format_ascii_left(self, spaces, index):
        return self.you.ascii_lines_back[index] + spaces[:-len(self.you.ascii_lines_back[index])]

    def add_top(self, spaces, dashes):
        string = ""
        string += f"+{dashes}-{dashes}+\n"
        string += f"|{self.add_enemy_name_padding()} {self.format_ascii_right(spaces, 0)}|\n"
        string += f"|{self.add_enemy_health_padding()} {self.format_ascii_right(spaces, 1)}|\n"
        string += f"|{spaces} {self.format_ascii_right(spaces, 2)}|\n"
        return string
    
    def add_bottom(self, spaces):
        string = ""
        string += f"|{self.format_ascii_left(spaces, -3)} {spaces}|\n"
        string += f"|{self.format_ascii_left(spaces, -2)} {self.add_you_name_padding()}|\n"
        string += f"|{self.format_ascii_left(spaces, -1)} {self.add_you_health_padding()}|\n"
        return string
    
    def add_moves(self, moves_list, dashes):
        string = ""
        string += f"+{dashes}" * 2 + "+\n"
        string += f"|{moves_list[0]}|{moves_list[1]}|\n"
        string += f"+{dashes}" * 2 + "+\n"
        string += f"|{moves_list[2]}|{moves_list[3]}|\n"
        string += f"+{dashes}" * 2 + "+\n"
        return string

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
        final_string += self.add_top(spaces, dashes)
        for r in range(3, len(self.enemy.ascii_lines_front)):
            final_string += f"|{self.format_ascii_left(spaces, r - 3)} {self.format_ascii_right(spaces, r)}|\n"
        final_string += self.add_bottom(spaces)
        final_string += self.add_moves(moves_list, dashes)
        return final_string
    
   
