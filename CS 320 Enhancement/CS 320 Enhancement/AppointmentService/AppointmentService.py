#Programmer: Hannah Frederick
#Date:09/20/2025
#Program Description: Utilize in-memory data structures to store, edit, and delete contact, task, and appointment information for a mobile application. Utilize Pytest unit testing to verify that all requirements are working as intended

import pytest
import sys
import os
import ipytest
ipytest.autoconfig()
from datetime import date

from Appointment import Appointment

class AppointmentService:

    #Create a list and set the currentId to 0 so we have a starting ID
    def __init__(self):
        self.appointment_list = []
        self.current_id = 0

    #adds an appointment and assigns it an Id
    def add_appointment(self, appointment_date, appointment_description):
        string_id = str(self.current_id)
        
        new_appointment = Appointment(string_id, appointment_date, appointment_description)
        self.appointment_list.append(new_appointment)

        self.current_id = self.current_id + 1

    #Deletes an appointment
    def delete_appointment(self, appointment_id):
        for appointment in self.appointment_list:
            if appointment.get_appointment_id() == appointment_id:
                self.appointment_list.remove(appointment)
                return True
        return False