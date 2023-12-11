from appointment import Appointment  # Importing the Appointment class from your previous file

def load_scheduled_appointments(filename, calendar):
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
