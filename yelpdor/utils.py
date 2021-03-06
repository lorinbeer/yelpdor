import os
import json


def load_eventset(name):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'res', 'textgen', name + '.json')
    fp = open(path).read()
    return json.loads(fp)

def load_name_recipes(name):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'res', 'textgen', name + '.json')
    fp = open(path).read()
    return json.loads(fp)