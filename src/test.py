import yaml
import os
from type import Type
import random
import pythemon
import battle
root_of_project = os.getcwd()
monsters = os.path.join(root_of_project + "/monsters/")
battle.make_yaml_from_csv()
test = pythemon.Pythemon(3)
front, back = test.get_ascii_string(monsters)
print(front)
print(back)