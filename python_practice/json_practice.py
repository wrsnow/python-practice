# Python program to read
# json file
import json
import os
# Opening JSON file

script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)

f = open('../../JSON_Files/disney_plus_content.json', "r")

# returns JSON object as
# a dictionary
data = json.loads(f.read())

# Iterating through the json
# list
headers = data[0].keys()

# for movie in data:
#   print(movie)

# Closing file
f.close()