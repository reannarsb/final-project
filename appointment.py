class Appointment:
    pass
    
def print_menu():
    """
    Print the main menu for Jojo's Hair Salon Appointment Manager.
    """
    print("Jojo's Hair Salon Appointment Manager")
    print("="*38)
    print("1) Schedule an appointment \n2) Find appointment by name \n3) Print calendar for a specific day \n4) Cancel an appointment \n9) Exit the system")
    selection = input("Enter your selection: ")

def create_weekly_calendar(appointment_calendar):
    """
    Creates a weekly calendar of appointments for each day and each hour.

    Args:
    appointment_calendar (list): The list to store the created Appointment objects.
    """
    # Clear the existing appointments in the calendar
    appointment_calendar.clear()

    # Loop through each day in the week
    for index in range(len(days_of_week)):
        # Loop through each hour of the day
        for time in range(the_first_hour, the_last_hour + 1):
            # Create a new Appointment object for the current day and time
            appointment = ap.Appointment(days_of_week[index], time)
            
            # Append the new Appointment to the calendar
            appointment_calendar.append(appointment)
