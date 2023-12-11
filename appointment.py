import csv
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


def __init__(self, client_name, client_phone, appt_type, day, time):
        self.client_name = client_name
        self.client_phone = client_phone
        self.appt_type = appt_type
        self.day = day
        self.time = time

    def is_scheduled(self):
        return self.appt_type is not None

    def format_record(self):
        return f"{self.client_name},{self.client_phone},{self.appt_type},{self.day},{self.time}\n"


def save_scheduled_appointments(appointment_list):
    filename = input("Enter appointment filename: ")

    try:
        with open(filename, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader) 

            for row in csv_reader:
                appointment = Appointment(
                    client_name=row[0],
                    client_phone=row[1],
                    appt_type=int(row[2]),
                    day=row[3],
                    time=row[4]
                )
                appointment_list.append(appointment)

        print(f"{len(appointment_list)} appointments loaded from {filename}")
        return len(appointment_list)

    except FileNotFoundError:
        print("File not found. Re-enter the filename.")
        return save_scheduled_appointments(appointment_list)



appointments = []
save_scheduled_appointments(appointments)


print("Appointments Scheduled:")
for appointment in appointments:
    print(appointment.client_name, appointment.client_phone, appointment.appt_type, appointment.day, appointment.time)

