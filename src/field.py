from pythemon import *

class Field():
    def __init__(self, you, enemy):
        self.field_width = 130
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

        moves = list(moves)
        moves = [name for name, _ in moves]
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
    
    def add_top_padding(self, spaces):
        # positive is enemy front sprite is bigger
        # negative is friendly back sprite is bigger
        if self.get_height_difference() <= 0:
            return ""
        string = ""
        bottom = self.get_height_difference()
        for i in range(2, bottom):
            string += f"|{spaces} {self.format_ascii_right(spaces, i)}|\n"
        return string
    
    def add_intersection(self, spaces):
        string = ""
        if self.get_height_difference() <= 0:
            for i in range(3, self.enemy.height_front):
                string += f"|{self.format_ascii_left(spaces, i - 3)} {self.format_ascii_right(spaces, i)}|\n"
            return string
        elif self.get_height_difference() > 0:
            for i in range(0, self.you.height_back - 2):
                string += f"|{self.format_ascii_left(spaces, i)} {self.format_ascii_right(spaces, i + self.get_height_difference())}|\n"
            return string
        else:
            return string

    def add_bottom_padding(self, spaces):
        if self.get_height_difference() >= 0:
            return ""
        string = ""
        top = self.get_height_difference()
        for i in range(top - 3, -2):
            string += f"|{self.format_ascii_left(spaces, i)} {spaces}|\n"
        return string

    def add_bottom(self, spaces):
        string = ""
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
    
    def get_height_difference(self):
        return self.enemy.height_front - self.you.height_back

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
        final_string += self.add_top_padding(spaces)
        final_string += self.add_intersection(spaces)
        final_string += self.add_bottom_padding(spaces)
        final_string += self.add_bottom(spaces)
        final_string += self.add_moves(moves_list, dashes)
        return final_string