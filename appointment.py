from appointment import Appointment  # Importing the Appointment class from your previous file

def load_scheduled_appointments(filename):
    appointments_loaded = 0
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    for line in lines:
        data = line.strip().split(',')
        client_name, client_phone, appnt_type_str, day_of_week, start_time_hour = data
        appnt_type = int(appnt_type_str)
        start_time_hour = int(start_time_hour)
        
        new_appointment = Appointment(day_of_week, start_time_hour)
        new_appointment.set_client_name(client_name)
        new_appointment.set_client_phone(client_phone)
        new_appointment.set_appt_type(appnt_type)
        appointments_loaded += 1
    
    return appointments_loaded
