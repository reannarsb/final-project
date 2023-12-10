class Appointment:
    pass

def find_appointment_by_time(appointment_list, day, start_hour):
    for appointment in appointment_list:
        if appointment.get_day_of_week().lower() == day.lower() and appointment.get_start_time_hour() == start_hour:
            return appointment 
    return None
