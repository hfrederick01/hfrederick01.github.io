#Programmer: Hannah Frederick
#Date:09/20/2025
#Program Description: Utilize in-memory data structures to store, edit, and delete contact, task, and appointment information for a mobile application. Utilize Pytest unit testing to verify that all requirements are working as intended

import pytest
import sys
import os
import ipytest
ipytest.autoconfig()

from Contact import Contact

class ContactService:

    #Create a list and set the currentId to 0 so we have a starting ID
    def __init__(self):
        self.contact_list = []
        self.current_id = 0

    #adds a contact and assigns it an Id
    def add_contact(self, first_name, last_name, phone_number,address):
        string_id = str(self.current_id)
        
        new_contact = Contact(string_id, first_name, last_name, phone_number, address)
        self.contact_list.append(new_contact)

        self.current_id = self.current_id + 1

    #Deletes a contact
    def delete_contact(self, contact_id):
        for contact in self.contact_list:
            if contact.get_contact_id() == contact_id:
                self.contact_list.remove(contact)
                return True
        return False

    #Updates the first name
    def update_first_name(self, contact_id, first_name):
        for contact in self.contact_list:
            if contact.get_contact_id() == contact_id:
                contact.set_first_name(first_name)
                return True
        return False

    #Updates the last name
    def update_last_name(self, contact_id, last_name):
        for contact in self.contact_list:
            if contact.get_contact_id() == contact_id:
                contact.set_last_name(last_name)
                return True
        return False

    #Updates the phone number
    def update_phone_number(self, contact_id, phone_number):
        for contact in self.contact_list:
            if contact.get_contact_id() == contact_id:
                contact.set_phone_number(phone_number)
                return True
        return False

    #Updates the address
    def update_address(self, contact_id, address):
        for contact in self.contact_list:
            if contact.get_contact_id() == contact_id:
                contact.set_address(address)
                return True
        return False