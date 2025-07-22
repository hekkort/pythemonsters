from field import *
import pythemon


def main():

    monsters = "/home/hekkort/workspace/github.com/hekkort/pythemonsters/monsters/"

    e_squirtle = pythemon.Pythemon("squirtle")
    f_squirtle = pythemon.Pythemon("squirtle")


    while e_squirtle.health > 0 and f_squirtle.health > 0:

        field = Field(f_squirtle, e_squirtle)
        print(field.draw_field())
        action = input("What kind of attack do you want to use? Type just the number: ")
        
        e_squirtle.health -= f_squirtle.use_move(action)




if __name__ == "__main__":
    main()
