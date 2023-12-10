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

def create_weekly_calendar():
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

