import csv
class Appointment:
    """
    Represents an appointment at Jojo's Hair Salon.
    """
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
the_first_hour = 9  # Assuming salon opens at 9 AM
the_last_hour = 17  # Assuming salon closes at 5 PM

    
def print_menu():
    """
    Print the main menu for Jojo's Hair Salon Appointment Manager.
    """
    print("Jojo's Hair Salon Appointment Manager")
    print("="*38)
    print("1) Schedule an appointment \n2) Find appointment by name \n3) Print calendar for a specific day \n4) Cancel an appointment \n9) Exit the system")
    selection = input("Enter your selection: ")

    def __init__(self, day_of_week, start_time_hour):
        """
        Initializes an Appointment object with default values.

        Args:
        day_of_week (str): The day of the week for the appointment.
        start_time_hour (int): The starting hour of the appointment.
        """
        self.__client_name = ''             # Initialize client name as an empty string
        self.__client_phone = ''            # Initialize client phone as an empty string
        self.__appnt_type = 0               # Initialize appointment type as 0 (Available)
        self.__day_of_week = day_of_week    # Set the day of the week
        self.__start_time_hour = start_time_hour  # Set the starting hour of the appointment

    def get_client_name(self):
        """
        Get the client's name for the appointment.

        Returns:
        str: The client's name.
        """
        return self.__client_name

    def get_client_phone(self):
        """
        Get the client's phone number for the appointment.

        Returns:
        str: The client's phone number.
        """
        return self.__client_phone

    def get_appt_type(self):
        """
        Get the type of appointment.

        Returns:
        int: The appointment type code.
        """
        return self.__appnt_type

    def get_start_time_hour(self):
        """
        Get the starting hour of the appointment.

        Returns:
        int: The starting hour.
        """
        return self.__start_time_hour

    def get_day_of_week(self):
        """
        Get the day of the week for the appointment.

        Returns:
        str: The day of the week.
        """
        return self.__day_of_week
    
    def get_end_time_hour(self):
        """
        Get the ending hour of the appointment (assumed to be one hour after the starting hour).

        Returns:
        int: The ending hour.
        """
        return self.__start_time_hour + 1
    
    def get_appt_type_desc(self):
        """
        Get the description of the appointment type.

        Returns:
        str: The description of the appointment type.
        """
        apptype_description = {
            0: "Available",
            1: "Mens Cut",
            2: "Ladies Cut",
            3: "Mens Colouring",
            4: "Ladies Colouring"
        }
        return apptype_description.get(self.__appnt_type, "Unknown Type")
        
    def set_client_name(self, client_name):
        """
        Set the client's name for the appointment.

        Args:
        client_name (str): The client's name.
        """
        self.__client_name = client_name

    def set_appt_type(self, appt_type):
        """
        Set the type of appointment.

        Args:
        appt_type (int): The appointment type code.
        """
        self.__appnt_type = appt_type

    def schedule(self, client_name, client_phone, appt_type):
        """
        Schedule the appointment with the given details.

        Args:
        client_name (str): The client's name.
        client_phone (str): The client's phone number.
        appt_type (int): The appointment type code.
        """
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appnt_type = appt_type

    def cancel(self):
        """
        Cancel the appointment by resetting client details and appointment type.
        """
        self.__client_name = ""
        self.__client_phone = ""
        self.__appnt_type = 0

    def format_record(self):
        """
        Format appointment details as a string.

        Returns:
        str: The formatted appointment details.
        """
        return f'{self.__client_name}, {self.__client_phone}, {self.__appnt_type}, {self.__day_of_week}, {self.__start_time_hour}'
    
    def __str__(self):
        """
        Get a formatted string representation of the appointment.

        Returns:
        str: The formatted string representation.
        """
        return f'{self.__client_name:<20}{self.__client_phone:<15}{self.__day_of_week:<10}{self.__start_time_hour:02}:00 - {self.get_end_time_hour():02}:00 {self.get_appt_type_desc()}'
    
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


def save_scheduled_appointments(appointment_list):
    # Get the filename from the user
    filename = input("Enter appointment filename: ")

    try:
        with open(filename, 'r', newline='') as file:
            # Read the CSV file using csv.reader
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Read the header row

            # Iterate through each row in the CSV and create Appointment objects
            for row in csv_reader:
                appointment = Appointment(
                    client_name=row[0],
                    client_phone=row[1],
                    appt_type=int(row[2]),
                    day=row[3],
                    time=row[4]
                )
                # Append the created Appointment object to the appointment_list
                appointment_list.append(appointment)

        print(f"{len(appointment_list)} appointments loaded from {filename}")
        return len(appointment_list)

    except FileNotFoundError:
        print("File not found. Re-enter the filename.")
        return save_scheduled_appointments(appointment_list)


# Creates an empty list to store appointments
appointments = []

# Calls the function to load appointments from the CSV file
save_scheduled_appointments(appointments)

# Print the loaded appointments
print("Appointments Scheduled:")
for appointment in appointments:
    print(appointment.client_name, appointment.client_phone, appointment.appt_type, appointment.day, appointment.time)

