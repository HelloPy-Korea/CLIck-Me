import json
import os

def load_config():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # config.py가 있는 폴더
    data_path = os.path.join(base_dir, "data.json")        # utils/data.json 경로
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)["developer"]