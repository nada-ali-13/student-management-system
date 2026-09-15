import json
import os


def load_data(file_path):
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("The file does not exist!")
        return []

def save_data(file_path, data):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        print("The file does not exist!")
        return []