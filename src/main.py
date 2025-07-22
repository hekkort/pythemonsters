from field import *
import pythemon

def main():

    f_bulbasaur = pythemon.Pythemon("bulbasaur")
    e_bulbasaur = pythemon.Pythemon("bulbasaur")

    while f_bulbasaur.health > 0 and e_bulbasaur.health > 0:

        field = Field(f_bulbasaur, e_bulbasaur)
        print(field.draw_field())
        action = input("What kind of attack do you want to use? Type just the number: ")
        
        e_bulbasaur.health -= f_bulbasaur.use_move(action)




if __name__ == "__main__":
    main()
