class Appointment:
    """
    Represents an appointment at Jojo's Hair Salon.
    """

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
    
    def create_weekly_calendar(self):
        """
        Create a weekly calendar of appointments for each day (Monday to Saturday) and each hour from 9 AM to 4 PM.

        Returns:
        list: A list of Appointment objects representing the weekly calendar.
        """
        calendar = []  # Initialize an empty list to store Appointment objects
        days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        # Loop through each day and hour to create and append Appointment objects to the calendar
        for day in days_of_the_week:
            for hour in range(9, 17):  # Hours range from 9 AM to 4 PM
                calendar.append(Appointment(day, hour))

        return calendar

