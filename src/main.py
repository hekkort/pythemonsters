from field import *
import pythemon


def main():

    monsters = "/home/hekkort/workspace/github.com/hekkort/pythemonsters/monsters/"

    pokemon = []
    count = 1

    while count < 12:
        pokemon.append(pythemon.Pythemon(count))
        count += 1
    field = Field(pokemon[5], pokemon[8])
    print(field.draw_field())




    # while charmander.health > 0 and squirtle.health > 0:

    #     field = Field(squirtle, charmander)
    #     print(field.draw_field())
    #     action = input("What kind of attack do you want to use? Type just the number: ")
        
    #     charmander.health -= squirtle.use_move(action)




if __name__ == "__main__":
    main()
