from data.json_store.json_store import load_data, users_file

def get_users():
    return load_data(users_file)