import csv
class Appointment:
    def __init__(self, day, time, description="Available"):
        self.day = day
        self.time = time
        self.description = description

def show_appointments_by_day(day_to_show, appointment_list):
    # Filters appointments for the specified day
    matching_appointments = [app for app in appointment_list if app.day == day_to_show]

    if not matching_appointments:
        #If the day dosn't match, then no appointment message appears
        print(f"No appointments found for {day_to_show}.")
        return

    print(f"Appointments for {day_to_show}:")
    for appointment in matching_appointments:
        # Prints appointment details in the specified format
        print(f"{appointment.day}\t{appointment.time}\t- {str(int(appointment.time.split(':')[0]) + 1)}:00\t{appointment.description}")


# appointments
appointments = [
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

# Get user input for the day and time
user_day = input("Enter the day for appointments: ")
user_time = input("Enter the time for appointments: ")

# Call the function to display appointments for the specified day
show_appointments_by_day(user_day, appointments)


 def __init__(self, client_name, client_phone, appt_type, day, time):
        self.client_name = client_name
        self.client_phone = client_phone
        self.appt_type = appt_type
        self.day = day
        self.time = time

    def is_scheduled(self):
        # Check if an appointment is scheduled by verifying if appt_type is not None
        return self.appt_type is not None

    def format_record(self):
        # Format the appointment record as a CSV line
        return f"{self.client_name},{self.client_phone},{self.appt_type},{self.day},{self.time}\n"


import csv
import os

class Appointment:
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

def file_exists(filename):
    return os.path.isfile(filename)

def read_csv_file(filename, appointment_list):
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

def save_scheduled_appointments(appointment_list):
    filename = input("Enter appointment filename: ")

    if not file_exists(filename):
        print("File not found. Re-enter the filename.")
        return save_scheduled_appointments(appointment_list)

    read_csv_file(filename, appointment_list)
    print(f"{len(appointment_list)} appointments loaded from {filename}")
    return len(appointment_list)

appointments = []
save_scheduled_appointments(appointments)

print("Appointments Scheduled:")
for appointment in appointments:
    print(appointment.client_name, appointment.client_phone, appointment.appt_type, appointment.day, appointment.time)
