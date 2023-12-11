import csv
class Appointment:
    """
    Represents an appointment at Jojo's Hair Salon.
    """
    def __init__(self, day_of_week, start_time_hour, appnt_type="0"): 
        """
        Initializes an Appointment object with default values.

        Args:
        day_of_week (str): The day of the week for the appointment.
        start_time_hour (int): The starting hour of the appointment.
        appnt_type = 0
        """
        self.__client_name = ''                  # Initialize client name as an empty string
        self.__client_phone = ''                 # Initialize client phone as an empty string
        self.__appnt_type = appnt_type           # Initialize appointment type as 0 (Available)
        self.__day_of_week = day_of_week         # Set the day of the week
        self.__start_time_hour = start_time_hour # Set the starting hour of the appointment

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
        return int(self.__appnt_type)

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
        return apptype_description
        
    def set_client_name(self, client_name):
        """
        Set the client's name for the appointment.

        Args:
        client_name (str): The client's name.
        """
        self.__client_name = client_name
        
    def set_client_phone(self, client_phone):
        """
        Set the clients phone for the appointment

        Args:
        client_phone (str): The clients phone.
        """
        self.__client_phone = client_phone
        

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
        appt_desc = self.get_appt_type_desc().get(int(self.__appnt_type), "Unknown Type")
        return f'{self.__client_name:<20}{self.__client_phone:<15}{self.__day_of_week:<10}{self.__start_time_hour:02}:00 - {self.get_end_time_hour():02}:00 {appt_desc}'


def print_menu():
    """
    Print the main menu for Jojo's Hair Salon Appointment Manager.
    """
    print("Jojo's Hair Salon Appointment Manager")
    print("="*38)
    print("1) Schedule an appointment \n2) Find appointment by name \n3) Print calendar for a specific day \n4) Cancel an appointment \n9) Exit the system")
    selection = input("Enter your selection: ")
    return selection
    
def create_weekly_calendar():
    """
    Creates a weekly calendar of appointments for each day and each hour.

    Args:
    appointment_calendar (list): The list to store the created Appointment objects.
    """
    # Clear the existing appointments in the calendar
    calendar = []  # Initialize an empty list to store Appointment objects
    days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # Loop through each day and hour to create and append Appointment objects to the calendar
    for day in days_of_the_week:
        for hour in range(9, 17):  # Hours range from 9 AM to 4 PM
            calendar.append(Appointment(day, hour))

    return calendar


def load_scheduled_appointments(filename, calendar):
    """
    Loads scheduled appointments from a file into the calendar.

    Args:
    filename (str): The name of the file containing appointment details.
    calendar (list): The list of Appointment objects representing the weekly calendar.

    Returns:
    int: The count of appointments successfully loaded.
    """
    appointments_loaded = 0
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    for line in lines:
        data = line.strip().split(',')
        client_name, client_phone, appnt_type_str, day_of_week, start_time_hour = data
        appnt_type = int(appnt_type_str)
        start_time_hour = int(start_time_hour)

        new_appointment = Appointment(day_of_week, start_time_hour)  # Initialize appointment
        new_appointment.set_client_name(client_name)
        new_appointment.set_client_phone(client_phone)
        new_appointment.set_appt_type(appnt_type)  # Set appointment type

        found_appointment = find_appointment_by_time(calendar, day_of_week, start_time_hour)
        if found_appointment:
            found_appointment.schedule(client_name, client_phone, appnt_type)

        appointments_loaded += 1
    
    return appointments_loaded

    
def find_appointment_by_time(calendar, day, start_time):
    """
    Finds an appointment in the calendar at a specified day and start time.

    Args:
    calendar (list): The list of Appointment objects representing the weekly calendar.
    day (str): The day of the appointment.
    start_time (int): The start time of the appointment.

    Returns:
    Appointment or None: The appointment object if found, otherwise None.
    """
    for appointment in calendar:
        if appointment.get_day_of_week().lower() == day.lower() and appointment.get_start_time_hour() == start_time:
            return appointment
    return None


def show_appointments_by_day(day_to_show, appointment_list):
    """
    Displays appointments for a specific day from the given list.

    Args:
    day_to_show (str): Day of the week to display appointments for.
    appointment_list (list): List of Appointment objects.
    """
    
    day_to_show = day_to_show.title()
    print(f"Appointments for {day_to_show}")
    print(f"{'Client Name':<20}{'Phone':<15}{'Day':<10}\t{'Start':<10}{'End':<8}\t{'Type'}")
    print("=" * 80)

    # Create a dictionary to hold appointments for the day
    appointments_for_day = {hour: "Available" for hour in range(9, 17)}

    # Update appointments in the dictionary
    for appointment in appointment_list:
        if appointment.get_day_of_week().capitalize() == day_to_show:
            start_hour = appointment.get_start_time_hour()
            appointments_for_day[start_hour] = appointment

    # Display appointments for the day
    for hour, appointment in appointments_for_day.items():
        if appointment == "Available":
            print(f"\t\t\t\t{day_to_show}\t\t{hour:02}:00 - {hour+1:02}:00  {appointment:>17}")
            print()
        else:
            print(f"{appointment.get_client_name()}\t{appointment.get_client_phone()}\t"
                  f"{appointment.get_day_of_week():<15}\t{hour:02}:00 - {hour+1:02}:00\t{appointment.get_appt_type_desc()[appointment.get_appt_type()]:>17}")
            print()

    
    
def save_scheduled_appointments(appointments, filename):
     """
    Saves scheduled appointments to a file.

    Args:
    appointments (list): The list of Appointment objects to be saved.
    filename (str): The name of the file to save the appointments.

    Returns:
    int: The count of appointments successfully saved.
    """
    file = open(filename, 'w', newline='')
    save_count = 0

    for appointment in appointments:
        if appointment.get_appt_type() != 0:
            file.write(appointment.format_record() + '\n')
            save_count += 1

    file.close()
    return save_count


def main():
    calendar = create_weekly_calendar()  # Set up a list of appointments for the week
    appointments = []  # Initialize an empty list to store scheduled appointments
    print("Starting the Appointment Manager System")
    print("Weekly calendar created")
    load_option = input("Would you like to load previously scheduled appointments from a file (Y/N)? ")
    if load_option.lower() == "y":
        file_found = False
        while not file_found:
            filename = input("Enter appointment filename: ")
            if filename == "appointments1.csv":
                file_found = True
                file = open(filename, 'r')
                lines = file.readlines()
                file.close()

                if lines:
                    for line in lines:
                        data = line.strip().split(',')
                        client_name, client_phone, appnt_type_str, day_of_week, start_time_hour = data
                        appnt_type = int(appnt_type_str)
                        start_time_hour = int(start_time_hour)

                        new_appointment = Appointment(day_of_week, start_time_hour)
                        new_appointment.set_client_name(client_name)
                        new_appointment.set_client_phone(client_phone)
                        new_appointment.set_appt_type(appnt_type)

                        appointments.append(new_appointment)

                    print(f"{len(appointments)} previously scheduled appointments have been loaded\n")
                else:
                    print("File not found. Re-enter appointment filename.\n")
            else:
                print("File not found. Re-enter appointment filename.\n")
    else:
        print()

    while True:
        selection = print_menu()  # Present the menu and get user's selection
        
        if selection == "1":  # Schedule an appointment
            print('\n** Schedule an Appointment **')
            day = input("What day: ")
            time = int(input("Enter start hour (24-hour clock): "))
            
            valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
            valid_hours = range(9, 17)
            if day.capitalize() not in valid_days or time not in valid_hours:
                print("Sorry, that time slot is not in the weekly calendar!\n")
            
            else:
                client_name = input("Client Name: ")
                client_phone = input("Client Phone: ")
                appointment = Appointment(day, time)
                appointment_types = appointment.get_appt_type_desc()

                print("Appointment types:")
                print("1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120")

                valid_appointment_types = [str(i) for i in range(1, 5)]
                appt_type = input("Type of Appointment: ")
                        
                if appt_type not in valid_appointment_types:
                    print("Sorry, that is not a valid appointment type!\n")
                
                else:
                    new_appointment = Appointment(day, time)
                    new_appointment.set_client_name(client_name)
                    new_appointment.set_client_phone(client_phone)
                    new_appointment.set_appt_type(appt_type)

                    appointments.append(new_appointment)
                    print(f"OK, {client_name}'s appointment is scheduled!\n")
                
                    existing_appointment = find_appointment_by_time(calendar ,day, start_time=" ")
                    if existing_appointment:
                        print(f"Sorry, that time slot is booked already!\n")

                    


        elif selection == "2":  
            print("\n** Find appointment by name **")
            name = input("Enter Client Name: ").lower()
            found_appointments = [app for app in appointments if name in app.get_client_name().lower()]
            print(f"Appointments for {name}")
            print(f"{'Client Name':<30}{'Phone':<20}{'Day':<15}{'Start':<10}{'End':<10}{'Type'}")
            print("=" * 100)

            for app in found_appointments:
                start_hour = app.get_start_time_hour()
                end_hour = start_hour + 1
                appointment_types = app.get_appt_type_desc()
                appt_desc = appointment_types.get(int(app.get_appt_type()), "Unknown Type")
                print(f"{app.get_client_name().title()} \t\t{app.get_client_phone()} \t{app.get_day_of_week().title()} \t"
                    f"{start_hour:02}:00 - {end_hour:02}:00 \t {appt_desc}")
                print()

        
        elif selection == "3":  # Print calendar for a specific day
            print('\n** Print calendar for a specific day **')
            user_day = input("Enter day of week: ")
            days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
            if user_day in days:
                f'Appointment for {user_day.upper()}'
                appointments_on_user_day = [app for app in appointments if app.get_day_of_week() == user_day.capitalize()]
                show_appointments_by_day(user_day, appointments_on_user_day)

            else: 
                f'Appointment for {user_day}'
                print(f"{'Client Name':<20}{'Phone':<15}{'Day':<10}\t{'Start':<10}{'End':<8}\t{'Type'}")
                print("=" * 80)
                print()

        elif selection == "4":  # Cancel an appointment
            print("\n** Cancel an appointment **")
            cancel_day = input("What day: ")
            cancel_time = int(input("Enter start hour (24-hour clock): "))
            found_appointment = False
            valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
            valid_hours = range(9, 17)
            if cancel_day.capitalize() not in valid_days or cancel_time not in valid_hours:
                print("Sorry, that time slot is not in the weekly calendar!\n")
            
            else:
            # Search for the appointment to cancel
                for app in appointments:
                    if app.get_day_of_week().lower() == cancel_day.lower() and app.get_start_time_hour() == cancel_time:
                        appointments.remove(app)
                        found_appointment = True
                        print(f"Appointment: {app.get_day_of_week()} {app.get_start_time_hour()}:00 - {app.get_end_time_hour()}:00 for {app.get_client_name()} has been cancelled!")
                        print()
                        break
            
                if not found_appointment:
                    # Check if the time slot is not booked or not in the weekly calendar
                    existing_times = [app.get_start_time_hour() for app in appointments if app.get_day_of_week().lower() == cancel_day.lower()]
                    if cancel_time not in range(9, 17):
                        print("Sorry, that time is outside the working hours.\n")
                    elif cancel_time not in existing_times:
                        print("That time slot isn't booked and doesn't need to be cancelled.\n")
                    else:
                        print("Sorry, that time slot is not in the weekly calendar!\n")
            
        elif selection == "9":  # Exit the system
            print("\n** Exit the system **")
            save_option = input("Would you like to save all scheduled appointments to a file (Y/N)? ")
            if save_option.lower() == "y":
                while True:
                    filename = input("Enter appointment filename: ")
                    if filename == "appointments1.csv":
                        overwrite = input("File already exists. Do you want to overwrite it (Y/N)? ").lower()
                        if overwrite == "y":
                            break
                    else:
                        break

                save_count = save_scheduled_appointments(appointments, filename)
                print(f"{save_count} scheduled appointments have been successfully saved")
            print("Good Bye!")
            break


        else:
            print("Invalid selection. Please choose a valid option.")

if __name__ == "__main__":
    main()

