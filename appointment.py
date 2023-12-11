class Appointment:
    name:input("name for the appointment:")
    date=input("day of appointment:")
    time=input("time of appointment:")
    
    def __init__(self):
        self.appointments = {}

    def schedule_appointment(self,name, date, time, details):
        appointment_time = f"{name}:{date} at {time}"
        if appointment_time in self.appointments:
            print(f"Appointment at {appointment_time} already exists.")
        else:
            self.appointments[appointment_time] = details
            print(f"Appointment scheduled at {appointment_time}: {details}")

    def find_appointment_time(self, date, time):
        appointment_time = (f"{date} at {time}")
        if appointment_time in self.appointments:
            print(f"Appointment at {appointment_time}: {self.appointments[appointment_time]}")
        else:
            print(f"No appointment found at {appointment_time}.")
    
    def find_appointment_by_name(appointments, name):
        for appointment in appointments:
            if appointment['name'] == name:
                return appointment
        


if __name__ == "__main__":
    scheduler = Appointment()

scheduler.find_appointment_time('2023-12-10',"14")
scheduler.find_appointment_by_name('Steven')


