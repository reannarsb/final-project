class Appointment:
    
    def __init__(self, day_of_week, start_time_hour):
        self.__client_name = ''
        self.__client_phone = ''
        self.__appnt_type = 0
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour

    def get_client_name(self):
        return self.__client_name

    def get_client_phone(self):
        return self.__client_phone

    def get_appt_type(self):
        return self.__appnt_type

    def get_start_time_hour(self):
        return self.__start_time_hour

    def get_day_of_week(self):
        return self.__day_of_week
    
    def get_end_time_hour(self):
        return self.get_end_time_hour + 1
    
    def get_appt_type_desc(self):
        apptype_description = {
        
        0: "Available",
        1: "Mens Cut",
        2: "Ladies Cut",
        3: "Mens Colouring",
        4: "Ladies Colouring"
        
        }
        return apptype_description(self.__appnt_type, "Type")
        
    def set_client_name(self, client_name):
        self.__client_name = client_name

    def set_appt_type(self, appt_type):
        self.__appnt_type = appt_type

    def schedule(self,client_name, client_phone, appt_type):
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appnt_type = appt_type

    def cancel(self):
        self.__client_name = ""
        self.__client_phone = ""
        self.__appnt_type = 0

    def format_record(self):
        return f'{self.__client_name}, {self.__client_phone}, {self.__appnt_type}, {self.__day_of_week}, {self.__start_time_hour}'
    
    def __str__(self):
        return f'{self.__client_name:<20}{self.__client_phone:<15}{self.__day_of_week:<10}{self.__start_time_hour:02}:00 - {self.get_end_time_hour}:00 {self.get_appt_type_desc()}'
    
    def create_weekly_calendar(self):
        calendar = []
        days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        
        for day in days_of_the_week:
            for hour in range(9, 17):
                calendar.append(Appointment(day, hour))

        return calendar
