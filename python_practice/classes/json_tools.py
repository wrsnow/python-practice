import json
import os


class JsonTools:
    @staticmethod
    def create_new_json(path, data):
        folder_path = "/".join(path.split("/")[:-1])
        os.makedirs(folder_path, exist_ok=True)
        with open(path, "w") as f:
            f.write(json.dumps(data, indent=2))

    @staticmethod
    def append_to_json( path, data):
        prev_data = None
        newdata = None
        prev_data_type= None
        try:
            with open(path, "r") as f:
                prev_data = json.loads(f.read())
            prev_data_type = type(prev_data)
        except FileNotFoundError:
            JsonTools.create_new_json(path,data)
            return

        if prev_data_type == dict and type(data) == dict:
            newdata = [prev_data, data]
        elif prev_data_type == dict and type(data) == list:
            newdata = [prev_data]
            newdata.extend(data)
        elif prev_data_type == list and type(data) == dict:
            newdata = []
            newdata.extend(prev_data)
            newdata.append(data)
        elif prev_data_type == list and type(data) == list:
            newdata = []
            newdata.extend(prev_data)
            newdata.extend(data)
        JsonTools.create_new_json(path, newdata)
