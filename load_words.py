""" Load json file into dictionary """
import json

with open('words/en/words.json', 'r') as f:

    python_dict = json.loads(f.read())

print(python_dict)
