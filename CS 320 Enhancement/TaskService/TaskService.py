#Programmer: Hannah Frederick
#Date:09/20/2025
#Program Description: Utilize in-memory data structures to store, edit, and delete contact, task, and appointment information for a mobile application. Utilize Pytest unit testing to verify that all requirements are working as intended

import pytest
import sys
import os
import ipytest
ipytest.autoconfig()

from Task import Task

class TaskService:

    #Create a list and set the currentId to 0 so we have a starting ID
    def __init__(self):
        self.task_list = []
        self.current_id = 0

    #adds a task and assigns it an Id
    def add_task(self, task_name, task_description):
        string_id = str(self.current_id)
        
        new_task = Task(string_id, task_name, task_description)
        self.task_list.append(new_task)

        self.current_id = self.current_id + 1

    #Deletes a task
    def delete_task(self, task_id):
        for task in self.task_list:
            if task.get_task_id() == task_id:
                self.task_list.remove(task)
                return True
        return False

    #Updates the task name
    def update_task_name(self, task_id, task_name):
        for task in self.task_list:
            if task.get_task_id() == task_id:
                task.set_task_name(task_name)
                return True
        return False

    #Updates the task description
    def update_task_description(self, task_id, task_description):
        for task in self.task_list:
            if task.get_task_id() == task_id:
                task.set_task_description(task_description)
                return True
        return False