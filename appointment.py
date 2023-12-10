class Appointment:
    pass

def print_menu():
    print("Jojo's Hair Salon Appointment Manager")
    print("="*38)
    print("1) Schedule an appointment \n2) Find appointment by name \n3) Print calendar for a specific day \n4) Cancel an appointment \n9) Exit the system")
    selection = input("Enter your selection: ")



def create_weekly_calendar():
    calendar = []
    days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', ‘Saturday’]

    for day in days_of_the_week:
        for hour in range(9, 17):
            calendar.append(Appointment(day, hour))

    return calendar

