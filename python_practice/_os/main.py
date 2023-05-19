import os
import re
import random

words = ['demonstrate', 'taste', 'produce', 'edition', 'quaint', 'impound', 'thought', 'approval', 'texture', 'brown', 'note', 'carpet', 'TRUE', 'architect', 'replace', 'pause', 'ceremony', 'clay', 'meal', 'product']


class Bcolors:
		HEADER = '\033[95m'
		BLUE = '\033[94m'
		CYAN = '\033[96m'
		GREEN = '\033[92m'
		YELLOW = '\033[93m'
		RED = '\033[91m'
		ENDC = '\033[0m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'


script_dir = os.path.dirname(os.path.abspath(__file__))
colored = Bcolors()

folder_path = "C:/path/to/folder"

os.chdir(script_dir)

def print_files(list):
	for el in list:
		if is_file(el):
			print(f"{colored.GREEN}{el}{colored.ENDC}")
		else:
			print(f"{colored.YELLOW}{el}{colored.ENDC}")

def is_file(string):
	return bool(re.search(r"\..*\w", string))

# try:
#   dir_content = os.listdir(path)
#   if len(dir_content) > 0:
#     print_files(dir_content)
#   else:
#     print("Folder is empty")
# except FileNotFoundError:
#   print(f"{colored.RED}File not found{colored.ENDC}")

def create_random_files():
	for i in range(0,40):
		base_name = f"{random.choice(words)}-{random.randint(0,200)}.txt"
		try:
			print(f"{colored.CYAN}[main] creating file: {base_name}{colored.ENDC}")
			f = open(f"{folder_path}/{base_name}", "x")
			print(f"{colored.GREEN}[main] {base_name} was created.{colored.ENDC}")
			f.close()
		except FileExistsError:
			print("file already exists.")



files = os.listdir(folder_path)
output_base = "secret"

def rename_file(path:str,filename:str,new_name:str):
	os.chdir(path)
	try:
		os.rename(filename, new_name)
	except:
		print(f"Something went wrong with file: {filename}")


def renameMany(files:list, basename:str)->None:
  counter = 0
  for file in files:
    counter+= 1
    file_ext = re.findall(r"\..*\w",file)[-1]
    rename_file(folder_path, file, f"{basename} {counter}{file_ext}")

renameMany(files, "OUTPUT")