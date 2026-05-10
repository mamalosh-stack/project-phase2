from data.json_store.json_store import load_data, save_data, appt_file

def get_appointments():
    return load_data(appt_file)

def add_appointment(appointment):
    appointments = load_data(appt_file)
    appointments.append(appointment)
    save_data(appt_file, appointments)