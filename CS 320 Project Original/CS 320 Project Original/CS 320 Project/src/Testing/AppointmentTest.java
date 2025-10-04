package Testing;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import AppointmentService.Appointment;

import java.util.Date;
import java.util.Calendar;

class AppointmentTest {

	@Test
	void testAppointmentClass() {
		Date appointmentDate = new Date();
		
		Appointment appointment = new Appointment("0123456789", appointmentDate, "Description under 50 characters");
		assertTrue(appointment.getAppointmentId().equals("0123456789"));
		assertTrue(appointment.getAppointmentDate().equals(appointmentDate));
		assertTrue(appointment.getAppointmentDescription().equals("Description under 50 characters"));
	}
	
	
	@Test
	void testAppointmentIdTooLong() {
		Date appointmentDate = new Date();
		
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Appointment("01234567890", appointmentDate, "Description under 50 characters");
		});
	}
	
	@Test
	void testAppointmentIdNull() {
		Date appointmentDate = new Date();
		
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Appointment(null, appointmentDate, "Description under 50 characters");
		});
	}
	
	@Test
	void testAppointmentDateInPast() {
		Calendar calendar = Calendar.getInstance();
		calendar.add(Calendar.DATE, -1);
		Date pastDate = calendar.getTime();
		
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Appointment("01234567890", pastDate, "Description under 50 characters");
		});
	}
	
	@Test
	void testAppointmentDateNull() {
		Date appointmentDate = new Date();
		
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Appointment("0123456789", null, "Description under 50 characters");
		});
	}
	
	@Test
	void testAppointmentDescriptionTooLong() {
		Date appointmentDate = new Date();
		
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Appointment("0123456789", appointmentDate, "This is an example of a description over 50 characters");
		});
	}
	
	@Test
	void testAppointmentDescriptionNull() {
		Date appointmentDate = new Date();
		
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Appointment("0123456789", appointmentDate, null);
		});
	}

}
