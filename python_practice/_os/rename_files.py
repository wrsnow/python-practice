import os
import re


## List all content inside the folder
dirfiles = os.listdir()

def is_file(string):
	return bool(re.search(r"\..*\w", string))

def rename_file(filename:str,new_name:str):
	try:
		os.rename(filename, new_name)
	except:
		print(f"Something went wrong with file: {filename}")

##
def renameMany(files:list, basename:str)->None:
	print("[app] started...")
	print("[app] renaming files...")
	counter = 0
	for file in files:
		counter+= 1
		file_ext = file.split(".")[-1]
		rename_file(file, f"{basename} {counter}.{file_ext}")
	print("[app] finished")

## filter the content of the folder and store only files
files = []

## check if it a file or a folder and add to files List
for file in dirfiles:
  if is_file(file):
    files.append(file)

## prompt the user to choose a name for the renamed files
desired_output = input("Output name: ")
print(files)
renameMany(files, desired_output)