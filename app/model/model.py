import os
import pandas as pd
import json
import uuid

class Model:
    def __init__(self):
        self.data_frame = pd.DataFrame(columns=['ID', 'Product Name', 'Quantity', 'Expiry Date', 'Tags'])
        self.inventory_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'inventory.json')

    def add_entry(self, name, quantity, expiry_date, tags):
        entry_id = str(uuid.uuid4())
        self.data_frame.loc[len(self.data_frame)] = [entry_id, name, quantity, expiry_date, tags]

    def delete_entry(self, entry_id):
        self.data_frame = self.data_frame[self.data_frame['ID'] != entry_id]

    def save_changes(self):
        data = self.data_frame.to_dict(orient='records')
        with open(self.inventory_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def load_data(self):
        with open(self.inventory_path, 'r') as json_file:
            data = json.load(json_file)
        self.data_frame = pd.DataFrame(data)
