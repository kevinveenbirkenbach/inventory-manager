# Inventory Manager

## About

The Inventory Manager was designed specifically to manage the ship inventory of the SY-Amy2 for her voyage between Alicante and Brest. It was created with the aim of helping the crew with better overview and planning of their resources, from deciding what to purchase to organizing what to cook.

This tool was written by Kevin Veen-Birkenbach. He can be contacted at kevin@veen.world and his personal website is [www.veen.world](https://www.veen.world).

This application would not have been possible without the help of Chat-GPT from OpenAI. You can find the three main conversations that led to the creation of this software in the links below:

- https://chat.openai.com/share/a6def7f5-2b90-4cc8-af7f-c0c75aa55522
- https://chat.openai.com/share/8f0e4cb3-7a45-46e4-8245-cfc1d5c222ed
- https://chat.openai.com/share/9d77e8a9-bf58-4026-bc27-4aa5be3a7673

## Installation and Setup

You can clone the project with the following command:

```bash
git clone https://github.com/username/InventoryManager.git
```

Navigate into the project directory:

```bash
cd InventoryManager
```

Ensure you have Python installed (preferably Python 3.9+).

Run the program with:

```bash
python main.py
```

## Usage

Upon launching the application, you are greeted with a table where each row represents an item in the inventory. The columns represent the 'UUID', 'Product Name', 'Quantity', 'Expiry Date', 'Location', and 'Tags'.

You can edit existing items directly in the table. Once you finish editing a field, the changes are automatically saved.

You can also add new items to the inventory. To do this, fill out the details of the item in the last row of the table (the one that's empty) and hit 'Enter'. The item gets added to the inventory and the changes are saved.

The 'Inc' and 'Dec' buttons can be used to increase and decrease the quantity of an item, respectively. The 'Delete' button can be used to remove an item from the inventory.

## License

This software is distributed under the GNU Affero General Public License Version 3, 19 November 2007. Please see the LICENSE file for more information.
