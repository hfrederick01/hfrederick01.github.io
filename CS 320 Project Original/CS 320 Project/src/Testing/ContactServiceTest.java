package Testing;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

import Contact_Service.ContactService;
import Contact_Service.Contact;

class ContactServiceTest {

	@AfterEach
	void tearDown() throws Exception {
		ContactService.contactArray.clear();
	}
	
	@Test
	void testAddContact() {
		ContactService contactService = new ContactService();
		contactService.addContact("hannah", "frederick", "1111111111", "30 Test Street");
		
		assertFalse(ContactService.contactArray.isEmpty());
		assertEquals("0", ContactService.contactArray.get(0).getContactId());
		assertEquals("hannah", ContactService.contactArray.get(0).getFirstName());
		assertEquals("frederick", ContactService.contactArray.get(0).getLastName());
		assertEquals("1111111111", ContactService.contactArray.get(0).getPhoneNumber());
		assertEquals("30 Test Street", ContactService.contactArray.get(0).getAddress());
		
	}
	
	@Test
	void testDeleteContact() {
		ContactService contactService = new ContactService();
		contactService.addContact("hannah", "frederick", "1111111111", "30 Test Street");
		
		
		assertFalse(ContactService.contactArray.isEmpty());
		
		assertEquals("hannah", contactService.contactArray.get(0).getFirstName());
		
		contactService.deleteContact("0");
		
	}
	
	@Test
	void testUpdateFirstName() {
		ContactService contactService = new ContactService();
		contactService.addContact("hannah", "frederick", "1111111111", "30 Test Street");
		
		assertEquals("hannah", ContactService.contactArray.get(0).getFirstName());
		
		contactService.updateFirstName("0", "notHannah");
		
		assertEquals("notHannah", contactService.contactArray.get(0).getFirstName());
	}
	
	@Test
	void testUpdateLastName() {
		ContactService contactService = new ContactService();
		contactService.addContact("hannah", "frederick", "1111111111", "30 Test Street");
		
		assertEquals("frederick", ContactService.contactArray.get(0).getLastName());
		
		contactService.updateLastName("0", "TestLast");
		
		assertEquals("TestLast", contactService.contactArray.get(0).getLastName());
	}
	
	@Test
	void testUpdatePhoneNumber() {
		ContactService contactService = new ContactService();
		contactService.addContact("hannah", "frederick", "1111111111", "30 Test Street");
		
		assertEquals("1111111111", ContactService.contactArray.get(0).getPhoneNumber());
		
		contactService.updatePhoneNumber("0", "2222222222");
		
		assertEquals("2222222222", contactService.contactArray.get(0).getPhoneNumber());
	}
	
	@Test
	void testUpdateAddress() {
		ContactService contactService = new ContactService();
		contactService.addContact("hannah", "frederick", "1111111111", "30 Test Street");
		
		assertEquals("30 Test Street", ContactService.contactArray.get(0).getAddress());
		
		contactService.updateAddress("0", "32 Test Road");
		
		assertEquals("32 Test Road", contactService.contactArray.get(0).getAddress());
	}


}
