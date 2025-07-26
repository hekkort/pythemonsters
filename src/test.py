import yaml
import os
from type import Type
import random
import pythemon
import battle
import make_yaml
root_of_project = os.getcwd()
monsters = os.path.join(root_of_project + "/monsters/")

make_yaml.make_yaml_from_csv()