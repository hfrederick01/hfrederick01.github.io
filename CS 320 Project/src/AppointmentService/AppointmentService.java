package AppointmentService;

import java.util.ArrayList;

import java.util.Date;

public class AppointmentService {
	
	//Create an array and set the currentId to 0 so we have a starting ID
	public static  ArrayList<Appointment> appointmentArray = new ArrayList<Appointment>();
	int currentId = 0;
	
	//adds an appointment and assigns it an Id
	public void addAppointment(Date appointmentDate, String appointmentDescription) {
		
		String stringId = Integer.toString(currentId);
		
		Appointment newAppointment = new Appointment(stringId, appointmentDate, appointmentDescription);
		appointmentArray.add(newAppointment);
		
		currentId = currentId + 1;
		
	}
	
	
	//Deletes an appointment
	public void deleteAppointment(String appointmentId) {

		for( int i = 0; i < appointmentArray.size(); i++) {
			if (appointmentArray.get(i).getAppointmentId().equals(appointmentId)) {
				appointmentArray.remove(i);
				break;
			}
		
		}
	}

}
