package Testing;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import Contact_Service.Contact;

class ContactTest {

	@Test
	void testContactClass() {
		Contact contact = new Contact("0123456789", "hannah", "frederick", "1111111111", "30 Test Street");
		assertTrue(contact.getContactId().equals("0123456789"));
		assertTrue(contact.getFirstName().equals("hannah"));
		assertTrue(contact.getLastName().equals("frederick"));
		assertTrue(contact.getPhoneNumber().equals("1111111111"));
		assertTrue(contact.getAddress().equals("30 Test Street"));
	}
	
	@Test
	void testContactIdTooLong() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("01234567890", "hannah", "frederick", "1111111111", "30 Test Street");
		});
	}
	
	@Test
	void testContactIdNull() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact(null, "hannah", "frederick", "1111111111", "30 Test Street");
		});
	}
	
	@Test
	void testFirstNameTooLong() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("0123456789", "hannahhannah", "frederick", "1111111111", "30 Test Street");
		});
	}
	
	@Test
	void testFirstNameNull() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("0123456789", null, "frederick", "1111111111", "30 Test Street");
		});
	}
	
	@Test
	void testLastNameTooLong() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("0123456789", "hannah", "frederickfrederick", "1111111111", "30 Test Street");
		});
	}
	
	@Test
	void testLastNameNull() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("0123456789", "hannah", null, "1111111111", "30 Test Street");
		});
	}
	
	@Test
	void testPhoneNumberTooLong() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("0123456789", "hannah", "frederick", "11111111111", "30 Test Street");
		});
	}
	
	@Test
	void testPhoneNumberNull() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("0123456789", "hannah", "frederick", null, "30 Test Street");
		});
	}
	
	@Test
	void testPhoneNumberTooShort() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("0123456789", "hannah", "frederick", "111111111", "30 Test Street");
		});
	}
	
	@Test
	void testAddressTooLong() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("0123456789", "hannah", "frederick", "1111111111", "30 Test Street Too Long Test Street");
		});
	}
	
	@Test
	void testAddressNull() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("0123456789", "hannah", "frederick", "1111111111", null);
		});
	}

}
