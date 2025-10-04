package Testing;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

import TaskService.TaskService;

class TaskServiceTest {

	@AfterEach
	void tearDown() throws Exception {
		TaskService.taskArray.clear();
	}
	
	@Test
	void testAddTask() {
		TaskService taskService = new TaskService();
		taskService.addTask("About 20 characters", "Description of less than 50 characters");
		
		assertFalse(TaskService.taskArray.isEmpty());
		
		assertEquals("0", TaskService.taskArray.get(0).getTaskId());
		assertEquals("About 20 characters", TaskService.taskArray.get(0).getTaskName());
		assertEquals("Description of less than 50 characters", TaskService.taskArray.get(0).getTaskDescription());	
	}
	
	@Test
	void testDeleteTask() {
		TaskService taskService = new TaskService();
		taskService.addTask("About 20 characters", "Description of less than 50 characters");
		
		
		assertFalse(TaskService.taskArray.isEmpty());
		
		assertEquals("About 20 characters", taskService.taskArray.get(0).getTaskName());
		
		taskService.deleteTask("0");
		
	}
	
	@Test
	void testUpdateTaskName() {
		TaskService taskService = new TaskService();
		taskService.addTask("About 20 characters", "Description of less than 50 characters");
		
		assertEquals("About 20 characters", TaskService.taskArray.get(0).getTaskName());
		
		taskService.updateTaskName("0", "New Task Name");
		
		assertEquals("New Task Name", taskService.taskArray.get(0).getTaskName());
	}
	
	@Test
	void testUpdateTaskDescription() {
		TaskService taskService = new TaskService();
		taskService.addTask("About 20 characters", "Description of less than 50 characters");
		
		assertEquals("Description of less than 50 characters", TaskService.taskArray.get(0).getTaskDescription());
		
		taskService.updateTaskDescription("0", "New Task Description");
		
		assertEquals("New Task Description", taskService.taskArray.get(0).getTaskDescription());
	}

}
