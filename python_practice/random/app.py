from glob import glob
import os
from cryptography.fernet import Fernet

script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, "output")
files = os.listdir(output_dir)

os.chdir(script_dir)

file = "my-file.txt"
key = Fernet.generate_key()

fernet = Fernet(key=key)

encMsg = fernet.encrypt(file.encode("sha-256"))

print(encMsg)

decMsg = fernet.decrypt(encMsg).decode()

print(decMsg)

# print(os.getcwd())

# with open("lambda-tests.py", "rb") as f:
#     print(f.read())


# for i in range(0, 20):
#     filename = "random-file"
#     file_ext = '.txt'
#     with open(f"{output_dir}/{filename}-{i}{file_ext}", "x") as f:
#         f.write(f"NEW FILE N: {i}")

# for file in files:
#     print(file)
