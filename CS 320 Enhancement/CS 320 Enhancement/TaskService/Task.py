#Programmer: Hannah Frederick
#Date:09/20/2025
#Program Description: Utilize in-memory data structures to store, edit, and delete contact, task, and appointment information for a mobile application. Utilize Pytest unit testing to verify that all requirements are working as intended

class Task:

    #Constructor
    def __init__(self, task_id, task_name, task_description):
        self.set_task_id(task_id)
        self.set_task_name(task_name)
        self.set_task_description(task_description)

    #Gets task ID
    def get_task_id(self):
        return self.task_id

    #Gets task name
    def get_task_name(self):
        return self.task_name

    #Gets task description
    def get_task_description(self):
        return self.task_description

    #Sets task ID if the ID is not null and if the ID less than 10 digits long
    def set_task_id(self, task_id):
        if task_id is None:
            raise Exception("Task ID null.")
        if len(task_id) > 10:
            raise Exception("Task ID too long.")
        else:
            self.task_id = task_id
            return True

    #Sets task name if the name is not null and if the name less than 20 characters long
    def set_task_name(self, task_name):
        if task_name is None:
            raise Exception("Task name null.")
        if len(task_name) > 20:
            raise Exception("Task name too long.")
        else:
            self.task_name = task_name
            return True

    #Sets task description if the description is not null and if the description less than 50 characters long
    def set_task_description(self, task_description):
        if task_description is None:
            raise Exception("Task description null.")
        if len(task_description) > 50:
            raise Exception("Task description too long.")
        else:
            self.task_description = task_description
            return True