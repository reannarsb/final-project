class Appointment:
    date=input("day of appointment:")
    time=input("time of appointment:")
    
    def __init__(self):
        self.appointments = {}

    def schedule_appointment(self, date, time, details):
        appointment_time = f"{date} at {time}"
        if appointment_time in self.appointments:
            print(f"Appointment at {appointment_time} already exists.")
        else:
            self.appointments[appointment_time] = details
            print(f"Appointment scheduled at {appointment_time}: {details}")

    def find_appointment(self, date, time):
        appointment_time = (f"{date} at {time}")
        if appointment_time in self.appointments:
            print(f"Appointment at {appointment_time}: {self.appointments[appointment_time]}")
        else:
            print(f"No appointment found at {appointment_time}.")


if __name__ == "__main__":
    scheduler = Appointment()

scheduler.find_appointment('2023-12-10',"14")

