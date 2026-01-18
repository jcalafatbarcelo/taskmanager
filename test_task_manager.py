import unittest
import os
import json
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()
        self.manager._tasks = []  # Clear tasks for testing
        self.manager._next_id = 1  # Reset next ID

    def tearDown(self):
        if os.path.exists(TaskManager.FILENAME):
            os.remove(TaskManager.FILENAME)

    def test_add_task(self):
        self.manager.add_task("Test task")
        self.assertEqual(len(self.manager._tasks), 1)
        self.assertEqual(self.manager._tasks[0].description, "Test task")

    def test_list_task(self):
        self.manager.add_task("Test task 1")
        self.manager.add_task("Test task 2")
        with self.assertLogs(level='INFO') as log:
            self.manager.list_task()
        self.assertIn("Test task 1", " ".join(log.output))
        self.assertIn("Test task 2", " ".join(log.output))

    def test_complete_task(self):
        self.manager.add_task("Test task")
        self.manager.complete_task(1)
        self.assertTrue(self.manager._tasks[0].completed)

    def test_delete_task(self):
        self.manager.add_task("Test task")
        self.manager.delete_task(1)
        self.assertEqual(len(self.manager._tasks), 0)

    def test_load_tasks(self):
        with open(TaskManager.FILENAME, "w") as file:
            json.dump([{ "id": 1, "description": "Test task", "completed": False }], file)
        self.manager.load_tasks()
        self.assertEqual(len(self.manager._tasks), 1)
        self.assertEqual(self.manager._tasks[0].description, "Test task")

    def test_save_tasks(self):
        self.manager.add_task("Test task")
        self.manager.save_tasks()
        with open(TaskManager.FILENAME, "r") as file:
            tasks = json.load(file)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['description'], "Test task")

if __name__ == '__main__':
    unittest.main()