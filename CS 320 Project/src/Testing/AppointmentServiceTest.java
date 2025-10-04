package Testing;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Date;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

import AppointmentService.Appointment;
import AppointmentService.AppointmentService;

class AppointmentServiceTest {

	@AfterEach
	void tearDown() throws Exception {
		AppointmentService.appointmentArray.clear();
	}
	
	@Test
	void testAddAppointment() {
		Date appointmentDate = new Date();
		
		AppointmentService appointmentService = new AppointmentService();
		appointmentService.addAppointment(appointmentDate, "Description under 50 characters");
		
		assertFalse(AppointmentService.appointmentArray.isEmpty());
		assertEquals("0", AppointmentService.appointmentArray.get(0).getAppointmentId());
		assertEquals(appointmentDate, AppointmentService.appointmentArray.get(0).getAppointmentDate());
		assertEquals("Description under 50 characters", AppointmentService.appointmentArray.get(0).getAppointmentDescription());
		
	}
	
	@Test
	void testDeleteAppointment() {
		Date appointmentDate = new Date();
		
		AppointmentService appointmentService = new AppointmentService();
		appointmentService.addAppointment(appointmentDate, "Description under 50 characters");
		
		
		assertFalse(AppointmentService.appointmentArray.isEmpty());
		
		assertEquals(appointmentDate, appointmentService.appointmentArray.get(0).getAppointmentDate());
		
		appointmentService.deleteAppointment("0");
		
	}

}
