import json
import os

fn = os.path.join(os.path.dirname(__file__), 'colornames.json')

json_data = open(fn).read()
data_list = json.loads(json_data)
by_name = {data["name"]: data["hex"] for data in data_list}
by_value = {data["hex"]: data["name"] for data in data_list}
