class Appointment:
    pass

def find_appointment_by_time(appointment_list, day, start_hour):
    for appointment in appointment_list:
        if appointment.get_day_of_week().lower() == day.lower() and appointment.get_start_time_hour() == start_hour:
            return appointment 
    return None


def show_appointments_by_day(appointment_list, day):
    matching_appointments = [appointment for appointment in appointment_list
                             if appointment.get_day_of_week().lower() == day.lower()]

    if matching_appointments:
        print("Appointments on {}:".format(day))
        for appointment in matching_appointments:
            print(appointment)
    else:
        print("No appointments found on {}.".format(day))
