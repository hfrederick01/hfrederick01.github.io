#Programmer: Hannah Frederick
#Date:09/20/2025
#Program Description: Utilize in-memory data structures to store, edit, and delete contact, task, and appointment information for a mobile application. Utilize Pytest unit testing to verify that all requirements are working as intended

class Contact:

    #Constructor
    def __init__(self, contact_id, first_name, last_name, phone_number, address):
        self.set_contact_id(contact_id)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_phone_number(phone_number)
        self.set_address(address)
        
    #Gets contact ID
    def get_contact_id(self):
        return self.contact_id

    #Gets first name
    def get_first_name(self):
        return self.first_name

    #Gets last name
    def get_last_name(self):
        return self.last_name

    #Gets phone number
    def get_phone_number(self):
        return self.phone_number

    #Gets address
    def get_address(self):
        return self.address

    #Sets contact ID if the ID is not null and if the ID less than 10 digits long
    def set_contact_id(self, contact_id):
        if contact_id is None:
            raise Exception("Contact ID null.")
        if len(contact_id) > 10:
            raise Exception("Contact ID too long.")
        else:
            self.contact_id = contact_id
            return True

    #Sets first name if the first name is not null and is less than 10 characters long
    def set_first_name(self, first_name):
        if first_name is None:
            raise Exception("First name null.")
        if len(first_name) > 10:
            raise Exception("First name too long.")
        else:
            self.first_name = first_name
            return True

    #Sets last name if the last name is not null and is less than 10 characters long
    def set_last_name(self, last_name):
        if last_name is None:
            raise Exception("Last name null.")
        if len(last_name) > 10:
            raise Exception("Last name too long.")
        else:
            self.last_name = last_name
            return True

    #Sets phone number if it is 10 digits long
    def set_phone_number(self, phone_number):
        if phone_number is None:
            raise Exception("Phone number null.")
        if len(phone_number) > 10:
            raise Exception("Phone number too long.")
        if len(phone_number) < 10:
            raise Exception("Phone number too short.")
        else:
            self.phone_number = phone_number
            return True

    #Sets address if the address is under 30 characters long
    def set_address(self, address):
        if address is None:
            raise Exception("Address null.")
        if len(address) > 30:
            raise Exception("Address too long.")
        else:
            self.address = address
            return True