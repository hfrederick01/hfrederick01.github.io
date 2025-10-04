package TaskService;

public class Task {
	
	private String taskId;
	private String taskName;
	private String taskDescription;
	
	//Constructor
	public Task(String taskId, String taskName, String taskDescription) {
		if(!setTaskId(taskId)) {
			throw new IllegalArgumentException("Invalid task ID.");
		}
		if(!setTaskName(taskName)) {
			throw new IllegalArgumentException("Invalid task name.");
		}
		if(!setTaskDescription(taskDescription)) {
			throw new IllegalArgumentException("Invalid task description");
		}
	}
	
	//Gets task ID
	public String getTaskId () {
		return taskId;
	}
	
	//Gets task name
	public String getTaskName () {
		return taskName;
	}
	
	//Gets task description
	public String getTaskDescription () {
		return taskDescription;
	}
	
	//Sets task ID if the ID is not null and if the ID less than 10 digits long
	public boolean setTaskId (String taskId) {
		if(taskId == null || taskId.length() > 10) {
			return false;
		}
		else {
			this.taskId = taskId;
			return true;
		}
	}
	
	//Sets task name if the name is not null and if the name less than 20 characters long
	public boolean setTaskName (String taskName) {
		if(taskName == null || taskName.length() > 20) {
			return false;
		}
		else {
			this.taskName = taskName;
			return true;
		}
	}
	
	//Sets task description if the description is not null and if the description less than 50 characters long
	public boolean setTaskDescription (String taskDescription) {
		if(taskDescription == null || taskDescription.length() > 50) {
			return false;
		}
		else {
			this.taskDescription = taskDescription;
			return true;
		}
	}

}
