package TaskService;

import java.util.ArrayList;

public class TaskService {
	
	//Create an array and set the currentId to 0 so we have a starting ID
	public static  ArrayList<Task> taskArray = new ArrayList<Task>();
	int currentId = 0;
		
	
	//adds a task and assigns it an Id
	public void addTask(String taskName, String taskDescription) {
		
		String stringId = Integer.toString(currentId);
		
		Task newTask = new Task(stringId, taskName, taskDescription);
		taskArray.add(newTask);
		
		currentId = currentId + 1;
		
	}
	
	//Deletes a task
	public void deleteTask(String taskId) {

		for( int i = 0; i < taskArray.size(); i++) {
			if (taskArray.get(i).getTaskId().equals(taskId)) {
				taskArray.remove(i);
				break;
			}
		
		}
	}
	
	//Updates the task name
	public void updateTaskName(String taskId, String taskName) {
		
		for( int i = 0; i < taskArray.size(); i++) {
			if (taskArray.get(i).getTaskId().equals(taskId)) {
				taskArray.get(i).setTaskName(taskName);
				break;
			}
		}
	}
	
	//Updates the task description
	public void updateTaskDescription(String taskId, String taskDescription) {
		
		for( int i = 0; i < taskArray.size(); i++) {
			if (taskArray.get(i).getTaskId().equals(taskId)) {
				taskArray.get(i).setTaskDescription(taskDescription);
				break;
			}
		}
	}

}
