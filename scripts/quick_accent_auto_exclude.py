# C :\Users\razor\AppData\Local\Microsoft\PowerToys\QuickAccent\settings.json

import json
import os
import sys
import wmi


def bytes_to_gb(bytes):
    return round(float(bytes) / 1024 / 1024 / 1024, 2)


f = wmi.WMI()

working_set_size_target = 1 * 1024 * 1024 * 1024  # size in GB
quick_accent_file_path = (
    "C:/Users/razor/AppData/Local/Microsoft/PowerToys/QuickAccent/settings.json"
)

wql = f"SELECT * FROM Win32_Process WHERE WorkingSetSize > {working_set_size_target}"

processes = []

for process in f.query(wql):
    # process.Terminate()
    processes.append(
        {
            "name": process.Name,
            "pid": process.ProcessId,
            "memory_gb": bytes_to_gb(process.WorkingSetSize),
            "memory": process.WorkingSetSize,
            "path": process.ExecutablePath
            if process.ExecutablePath
            else "N/A",  # Handle None values
        }
    )

processes = sorted(processes, key=lambda x: x["memory_gb"], reverse=True)

if len(processes) <= 0:
    print("No processes found")
    exit(0)

process_with_highest_memory = processes[0]


""" check if the file exists """

if not os.path.exists(quick_accent_file_path):
    print(f"file {quick_accent_file_path} does not exist")
    exit(0)

with open(quick_accent_file_path, "r") as f:
    data = json.load(f)

    excluded_list = data["properties"]["excluded_apps"]["value"].split("\r")

    if process_with_highest_memory["name"] in excluded_list:
        print(f"{process_with_highest_memory['name']} is already in the excluded list")
        exit(0)

    """ remove duplicates from the list """
    excluded_list = list(set(excluded_list))

    excluded_list.append(process_with_highest_memory["name"])

    data["properties"]["excluded_apps"]["value"] = "\r".join(excluded_list)

    with open(quick_accent_file_path, "w") as f:
        f.write(json.dumps(data, indent=2))

print(f"{process_with_highest_memory['name']} was added to the excluded list")
