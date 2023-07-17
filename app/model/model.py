import os
import pandas as pd
import json
import uuid
import datetime
import glob

class Model:
    def __init__(self, data_dir=None):
        self.data_frame = pd.DataFrame(columns=['uuid', 'name', 'quantity', 'expiry_date', 'location', 'tags'])
        if data_dir is None:
            self.inventory_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
        else:
            self.inventory_dir = data_dir
            
    def add_entry(self, name, quantity, expiry_date, location, tags):
        entry_id = str(uuid.uuid4())
        tags_list = [tag.strip() for tag in tags.split(',')]
        self.data_frame.loc[len(self.data_frame)] = [entry_id, name, quantity, expiry_date, location, tags_list]

    def delete_entry(self, entry_id):
        self.data_frame = self.data_frame[self.data_frame['uuid'] != entry_id]

    def save_changes(self):
        data = self.data_frame.to_dict(orient='records')
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        inventory_path = os.path.join(self.inventory_dir, f'inventory.{timestamp}.json')
        with open(inventory_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def load_data(self):
        list_of_files = glob.glob(self.inventory_dir + '/inventory.*.json')
        if not list_of_files:
            self.data_frame = pd.DataFrame(columns=['uuid', 'name', 'quantity', 'expiry_date', 'location', 'tags'])
        else:
            latest_file = max(list_of_files, key=lambda x: x.split('.')[-2])  # -2 to get the timestamp part of the filename
            print(latest_file)
            with open(latest_file, 'r') as json_file:
                data = json.load(json_file)
            self.data_frame = pd.DataFrame(data)

