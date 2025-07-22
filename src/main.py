from field import *
import pythemon

def main():


    bulbasaur = pythemon.Pythemon("bulbasaur")

    # for b in bulbasaur.ascii_lines_back:
    #     print(b)
    # for b in bulbasaur.ascii_lines_front:
    #     print(b)

    field = Field(96, bulbasaur, bulbasaur)
    print(bulbasaur.name)
    print(field.add_enemy_name_padding())
    



if __name__ == "__main__":
    main()
