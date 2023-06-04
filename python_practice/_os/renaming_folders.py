import os

"""
Purpose: Rename folders and desired files in NextJS format, so I can
use them in NextJS new 'App' folder;

Script to  rename many folders and files.. Check if a folder contents
includes index.tsx if does, then it will rename to page.tsx
then before starting a new iteration it will check if the folder name
starts with an uppercase, it will then convert it to lowercase
otherwise just pass
"""


folder_path = "c:/users/username/desktop/input"


def open_folder(path):
    print(f"Acessing path: {path}")
    folder_content = os.listdir(path)
    print(f"Path contents: {folder_content}")
    for file in folder_content:
        if str(file).startswith("index.tsx"):
            os.rename(f"{path}/{file}", f"{path}/page.tsx")
            print(f"File in {path} was renamed succesfully.")
    print("--------------------------------------")
    print()


def start(folder_path):
    os.chdir(folder_path)
    for i in os.listdir():
        if os.path.isdir(i):
            open_folder(i)
            if i[0].isupper():
                newname = str(i).lower()
                os.rename(i, newname)


start(folder_path=folder_path)
