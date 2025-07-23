from field import *
import pythemon


def main():

    monsters = "/home/hekkort/workspace/github.com/hekkort/pythemonsters/monsters/"

    bulbasaur = pythemon.Pythemon(1)
    charmander = pythemon.Pythemon(4)
    squirtle = pythemon.Pythemon(7)
    mewtwo = pythemon.Pythemon(150)
    raticate = pythemon.Pythemon(20)
    farfetched = pythemon.Pythemon(83)
    clefable = pythemon.Pythemon(40)
    venusaur = pythemon.Pythemon(3)
    charizard = pythemon.Pythemon(6)

    field = Field(charmander, bulbasaur)
    print(field.draw_field())




    # while charmander.health > 0 and squirtle.health > 0:

    #     field = Field(squirtle, charmander)
    #     print(field.draw_field())
    #     action = input("What kind of attack do you want to use? Type just the number: ")
        
    #     charmander.health -= squirtle.use_move(action)




if __name__ == "__main__":
    main()
