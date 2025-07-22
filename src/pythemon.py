class Pythemon():
    def __init__(self, species, moves=None):
        
        self.species = species
        if moves != None:
            for i in range(len(moves)):
                self.moves[i] = f" {i + 1}. {moves[i]}"

    def make_ascii_of_monster(filename):
        with open(filename, "r") as file:
            lines = file.readlines()
        return lines        