from data.json_store.json_store import load_data, save_data, appt_file

def get_appointments():
    return load_data(appt_file)

def add_appointment(appointment):
    appointments = load_data(appt_file)
    appointments.append(appointment)
    save_data(appt_file, appointments)

from datetime import datetime

def get_next_appointment_id(appointments):
    if len(appointments) == 0:
        return 1

    max_id = 0
    for appt in appointments:
        if appt["id"] > max_id:
            max_id = appt["id"]

    return max_id + 1


def get_user_appointments(appointments, user_email):
    user_appts = []

    for appt in appointments:
        if appt.get("client_email") == user_email:
            user_appts.append(appt)

    return user_appts


def is_past_appointment(appt):
    appointment_datetime = datetime.strptime(
        f"{appt['date']} {appt['time']}",
        "%Y-%m-%d %I:%M %p"
    )

    return appointment_datetime < datetime.now()