from data.json_store.json_store import load_data, save_data, inventory_file

def get_inventory():
    return load_data(inventory_file)

def update_inventory(data):
    save_data(inventory_file, data)