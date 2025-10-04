#Programmer: Hannah Frederick
#Date:09/20/2025
#Program Description: Utilize in-memory data structures to store, edit, and delete contact, task, and appointment information for a mobile application. Utilize Pytest unit testing to verify that all requirements are working as intended

from datetime import date

class Appointment:

    #Constructor
    def __init__(self, appointment_id, appointment_date, appointment_description):
        self.set_appointment_id(appointment_id)
        self.set_appointment_date(appointment_date)
        self.set_appointment_description(appointment_description)
           
    #Gets appointment ID
    def get_appointment_id(self):
        return self.appointment_id

    #Gets appointment name
    def get_appointment_date(self):
        return self.appointment_date

    #Gets appointment description
    def get_appointment_description(self):
        return self.appointment_description

    #Sets appointment ID if the ID is not null and if the ID less than 10 digits long
    def set_appointment_id(self, appointment_id):
        if appointment_id is None:
            raise Exception("Appointment ID null.")
        if len(appointment_id) > 10:
            raise Exception("Appointment ID too long.")
        else:
            self.appointment_id = appointment_id
            return True

    #Sets appointment date if the date is not null and if the date is not in the past
    def set_appointment_date(self, appointment_date):
        if appointment_date is None:
            raise Exception("Appointment date null.")
        if appointment_date < date.today():
            raise Exception("Appointment date in the past.")
        else:
            self.appointment_date = appointment_date
            return True

    #Sets appointment description if the description is not null and if the description less than 50 characters long
    def set_appointment_description(self, appointment_description):
        if appointment_description is None:
            raise Exception("Appointment description null.")
        if len(appointment_description) > 50:
            raise Exception("Appointment description too long.")
        else:
            self.appointment_description = appointment_description
            return True