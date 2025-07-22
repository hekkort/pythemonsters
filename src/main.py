from field import *
import pythemon

def main():


    bulbasaur = pythemon.Pythemon("bulbasaur")

    for b in bulbasaur.ascii_lines_back:
        print(b)
    for b in bulbasaur.ascii_lines_front:
        print(b)

    print(len(bulbasaur.ascii_lines_back))
    print(len(bulbasaur.ascii_lines_back[0]))
    print(len(bulbasaur.ascii_lines_front))
    print(len(bulbasaur.ascii_lines_front[0]))

    field = Field(bulbasaur, bulbasaur)
    



if __name__ == "__main__":
    main()
