import pandas as pd
import json

class Model:
    def __init__(self):
        self.data_frame = pd.DataFrame(columns=['Product Name', 'Quantity', 'Expiry Date', 'Tags'])

    def add_entry(self, name, quantity, expiry_date, tags):
        self.data_frame.loc[len(self.data_frame)] = [name, quantity, expiry_date, tags]

    def delete_entry(self, del_product):
        self.data_frame = self.data_frame[self.data_frame['Product Name'] != del_product]

    def save_changes(self):
        data = self.data_frame.to_dict(orient='records')
        with open('../data/inventory.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def load_data(self):
        with open('../data/inventory.json', 'r') as json_file:
            data = json.load(json_file)
        self.data_frame = pd.DataFrame(data)