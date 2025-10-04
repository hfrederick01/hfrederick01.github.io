package Contact_Service;

public class Contact {
	
	private String contactId;
	private String firstName;
	private String lastName;
	private String phoneNumber;
	private String address;
	
	//Constructor
	public Contact(String contactId, String firstName, String lastName, String phoneNumber, String address) {
		if(!setContactId(contactId)) {
			throw new IllegalArgumentException("Invalid contact ID.");
		}
		if(!setFirstName(firstName)) {
			throw new IllegalArgumentException("Invalid first name.");
		}
		if(!setLastName(lastName)) {
			throw new IllegalArgumentException("Invalid last name.");
		}
		if(!setPhoneNumber(phoneNumber)) {
			throw new IllegalArgumentException("Invalid phone number.");
		}
		if(!setAddress(address)) {
			throw new IllegalArgumentException("Invalid address.");
		}
	}

	//Gets contact ID
	public String getContactId () {
		return contactId;
	}
	
	//Gets first name
	public String getFirstName () {
		return firstName;
	}
	
	//Gets last name
	public String getLastName () {
		return lastName;
	}
	
	//Gets phone number
	public String getPhoneNumber () {
		return phoneNumber;
	}
	
	//Gets address
	public String getAddress () {
		return address;
	}
	
	//Sets contact ID if the ID is not null and if the ID less than 10 digits long
	public boolean setContactId (String contactId) {
		if(contactId == null || contactId.length() > 10) {
			return false;
		}
		else {
			this.contactId = contactId;
			return true;
		}
	}
	
	//Sets first name if the first name is not null and if the first name less than 10 characters long
	public boolean setFirstName (String firstName) {
		if(firstName == null || firstName.length() > 10) {
			return false;
		}
		else {
			this.firstName = firstName;
			return true;
		}
	}
	
	//Sets last name if the last name is not null and if the last name less than 10 characters long
	public boolean setLastName (String lastName) {
		if(lastName == null || lastName.length() > 10) {
			return false;
		}
		else {
			this.lastName = lastName;
			return true;
		}
	}
	
	//Sets phone number if the phone number is not null and is exactly 10 digits long
	public boolean setPhoneNumber (String phoneNumber) {
		if( phoneNumber == null || phoneNumber.length() != 10) {
			return false;
		}
		else {
			this.phoneNumber = phoneNumber;
			return true;
		}
	}
	
	//Sets address if the address is not null and is less than 30 characters
	public boolean setAddress (String address) {
		if(address == null || address.length() > 30) {
			return false;
		}
		else {
			this.address = address;
			return true;
		}
	}
}
