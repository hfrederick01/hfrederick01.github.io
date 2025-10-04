package Testing;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import TaskService.Task;

class TaskTest {

	@Test
	void testTaskClass() {
		Task task = new Task("0123456789", "About 20 characters", "Description of less than 50 characters");
		assertTrue(task.getTaskId().equals("0123456789"));
		assertTrue(task.getTaskName().equals("About 20 characters"));
		assertTrue(task.getTaskDescription().equals("Description of less than 50 characters"));
		
	}
	
	@Test
	void testTaskIdTooLong() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Task("01234567890", "About 20 characters", "Description of less than 50 characters");
		});
	}
	
	@Test
	void testTestIdNull() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Task(null, "About 20 characters", "Description of less than 50 characters");
		});
	}
	
	@Test
	void testTaskNameTooLong() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Task("0123456789", "More than 20 characters", "Description of less than 50 characters");
		});
	}
	
	@Test
	void testTestNameNull() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Task("0123456789", null, "Description of less than 50 characters");
		});
	}
	
	@Test
	void testTaskDescriptionTooLong() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Task("0123456789", "About 20 characters", "Description of more than 50 characters is in this place");
		});
	}
	
	@Test
	void testTestDescriptionNull() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Task("0123456789", "About 20 characters", null);
		});
	}

}
