import random
import json
import os
from pathlib import Path
from icecream import ic


def getConfigVariables():
    ENV = os.getenv('ENV', 'dev')
    print(ic.format(ENV))
    path = Path(f"config/{ENV}.json").absolute()
    with open(path) as json_data_file:
        return json.load(json_data_file)


def getClassNameForTodoCard():
    return random.choice(['bg-warning',
                          'bg-success',
                          'bg-info',
                          'bg-danger',
                          'bg-light'])


def attachColorClassName(collectionData):
    return [{**dataObj, **{'colorClassName': getClassNameForTodoCard()}} for dataObj in collectionData]
