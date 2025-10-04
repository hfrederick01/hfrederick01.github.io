package Contact_Service;

import java.util.ArrayList;

public class ContactService {
	
	//Create an array and set the currentId to 0 so we have a starting ID
	public static  ArrayList<Contact> contactArray = new ArrayList<Contact>();
	int currentId = 0;
	
	//adds a contact and assigns it an Id
	public void addContact(String firstName, String lastName, String phoneNumber, String address) {
		
		String stringId = Integer.toString(currentId);
		
		Contact newContact = new Contact(stringId, firstName, lastName, phoneNumber, address);
		contactArray.add(newContact);
		
		currentId = currentId + 1;
		
	}
	
	
	//Deletes a contact
	public void deleteContact(String contactId) {

		for( int i = 0; i < contactArray.size(); i++) {
			if (contactArray.get(i).getContactId().equals(contactId)) {
				contactArray.remove(i);
				break;
			}
		
		}
	}
	
	//Updates the first name
	public void updateFirstName(String contactId, String firstName) {
		
		for( int i = 0; i < contactArray.size(); i++) {
			if (contactArray.get(i).getContactId().equals(contactId)) {
				contactArray.get(i).setFirstName(firstName);
				break;
			}
		}
	}
	
	//Updates the last name
	public void updateLastName(String contactId, String lastName) {
		
		for( int i = 0; i < contactArray.size(); i++) {
			if (contactArray.get(i).getContactId().equals(contactId)) {
				contactArray.get(i).setLastName(lastName);
				break;
			}
		}
	}
	
	//Updates the phone number
	public void updatePhoneNumber(String contactId, String phoneNumber) {
		
		for( int i = 0; i < contactArray.size(); i++) {
			if (contactArray.get(i).getContactId().equals(contactId)) {
				contactArray.get(i).setPhoneNumber(phoneNumber);
				break;
			}
		}
	}
	
	//Updates the address
	public void updateAddress(String contactId, String address) {
		
		for( int i = 0; i < contactArray.size(); i++) {
			if (contactArray.get(i).getContactId().equals(contactId)) {
				contactArray.get(i).setAddress(address);
				break;
			}
		}
	}
	
}