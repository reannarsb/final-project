from appointment import Appointment  # Importing the Appointment class from your previous file

def load_scheduled_appointments(filename, calendar):
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
        
        found_appointment = find_appointment_by_time(calendar, day_of_week, start_time_hour)
        if found_appointment:
            found_appointment.schedule(client_name, client_phone, appnt_type)

        appointments_loaded += 1
    
    return appointments_loaded

def find_appointment_by_time(calendar, day, start_time):
    for appt in calendar:
        if appt.get_day_of_week() == day and appt.get_start_time_hour() == start_time:
            return appt
    return None
