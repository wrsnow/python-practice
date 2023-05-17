import csv
import os
import json


script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)

f = open('../../JSON_Files/disney_plus_content.json', "r")

# returns JSON object as
# a dictionary
data = json.loads(f.read())

# Iterating through the json
# list
headers = data[0].keys()

with open("disney_content.csv", 'w', newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for movie in data:
        values = movie.values()
        writer.writerow(values)


# for movie in data:
#   print(movie)

# Closing file
f.close()