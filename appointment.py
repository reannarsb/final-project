class Appointment:
    def __init__(self, day, time, description="Available"):
        self.day = day
        self.time = time
        self.description = description

def show_appointments_by_day(day_to_show, appointment_list):
    """
    Displays appointments for a specific day from the given list.

    Args:
    day_to_show (str): Day of the week to display appointments for.
    appointment_list (list): List of Appointment objects.
    """
    # Filter appointments for the specified day
    matching_appointments = [app for app in appointment_list if app.day == day_to_show]

    # If no matching appointments, print a message and return
    if not matching_appointments:
        print(f"No appointments found for {day_to_show}.")
        return

    # Print header for the appointment table
    print(f"Appointments for {day_to_show}:")
    
    # Display each matching appointment with formatted details
    for appointment in matching_appointments:
        print(f"{appointment.day}\t{appointment.time}\t- {str(int(appointment.time.split(':')[0]) + 1)}:00\t{appointment.description}")



appointments = [
    # List of Appointment objects representing the salon's schedule
    Appointment(day="Monday", time="09:00", description="Available"),
    Appointment(day="Monday", time="10:00", description="Available"),
    Appointment(day="Monday", time="11:00", description="Available"),
    Appointment(day="Monday", time="12:00", description="Available"),
    Appointment(day="Monday", time="13:00", description="Available"),
    Appointment(day="Monday", time="14:00", description="Available"),
    Appointment(day="Monday", time="15:00", description="Available"),
    Appointment(day="Monday", time="16:00", description="Ladies Cut"),
    Appointment(day="Tuesday", time="09:00", description="Available"),
    Appointment(day="Tuesday", time="10:00", description="Available"),
    Appointment(day="Tuesday", time="11:00", description="Mens Cut"),
    Appointment(day="Tuesday", time="12:00", description="Available"),
    Appointment(day="Tuesday", time="13:00", description="Ladies Colouring"),
    Appointment(day="Tuesday", time="14:00", description="Available"),
    Appointment(day="Tuesday", time="15:00", description="Available"),
    Appointment(day="Tuesday", time="16:00", description="Available"),
    Appointment(day="Thursday", time="09:00", description="Available"),
    Appointment(day="Thursday", time="10:00", description="Available"),
    Appointment(day="Thursday", time="11:00", description="Mens Cut"),
    Appointment(day="Thursday", time="12:00", description="Available"),
    Appointment(day="Thursday", time="13:00", description="Ladies Colouring"),
    Appointment(day="Thursday", time="14:00", description="Available"),
    Appointment(day="Thursday", time="15:00", description="Available"),
    Appointment(day="Thursday", time="16:00", description="Available"),
    Appointment(day="Thursday", time="17:00", description="Available"),
    Appointment(day="Friday", time="9:00", description="Ladies Cut"),
    Appointment(day="Friday", time="10:00", description="Available"),
    Appointment(day="Friday", time="11:00", description="Available"),
    Appointment(day="Friday", time="12:00", description="Available"),
    Appointment(day="Friday", time="13:00", description="Available"),
    Appointment(day="Friday", time="14:00", description="Available"),
    Appointment(day="Friday", time="15:00", description="Available"),
    Appointment(day="Friday", time="16:00", description="Available"),
    Appointment(day="Saturday", time="10:00", description="Ladies Cut"),
]

user_day = input("Enter the day for appointments: ")  # Prompt user for a day
user_time = input("Enter the time for appointments: ")  # Prompt user for a time

show_appointments_by_day(user_day, appointments)  # Display appointments for the specified day
