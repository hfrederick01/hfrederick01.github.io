package AppointmentService;

import java.util.Date;

public class Appointment {
	private String appointmentId;
	private Date appointmentDate;
	private String appointmentDescription;
	
	//Constructor
	public Appointment(String appointmentId, Date appointmentDate, String appointmentDescription) {
		if(!setAppointmentId(appointmentId)) {
			throw new IllegalArgumentException("Invalid appointment ID.");
		}
		if(!setAppointmentDate(appointmentDate)) {
			throw new IllegalArgumentException("Invalid appointment date.");
		}
		if(!setAppointmentDescription(appointmentDescription)) {
			throw new IllegalArgumentException("Invalid appointment description.");
		}
	}
	
	//Gets appointment ID
	public String getAppointmentId () {
		return appointmentId;
	}
	
	//Gets appointment date
	public Date getAppointmentDate () {
		return appointmentDate;
	}
	
	//Gets appointment description
	public String getAppointmentDescription () {
		return appointmentDescription;
	}
	
	//Sets appointment ID if the ID is not null and if the ID less than 10 digits long
	public boolean setAppointmentId (String appointmentId) {
		if(appointmentId == null || appointmentId.length() > 10) {
			return false;
		}
		else {
			this.appointmentId = appointmentId;
			return true;
		}
	}
	
	//Sets appointment date if the date is not null and if the date is not in the past
	public boolean setAppointmentDate (Date appointmentDate) {
		if(appointmentDate == null || appointmentDate.before(new Date())) {
			return false;
		}
		else {
			this.appointmentDate = appointmentDate;
			return true;
		}
	}
	
	//Sets appointment description if the description is not null and is less than 50 characters long
	public boolean setAppointmentDescription (String appointmentDescription) {
		if(appointmentDescription == null || appointmentDescription.length() > 50) {
			return false;
		}
		else {
			this.appointmentDescription = appointmentDescription;
			return true;
		}
	}


}
