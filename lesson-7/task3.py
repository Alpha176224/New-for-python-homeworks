import json
import csv

class Task:
    def __init__(self, task_id, title, description, due_date=None, status='Pending'):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "Task ID": self.task_id,
            "Title": self.title,
            "Description": self.description,
            "Due Date": self.due_date,
            "Status": self.status
        }

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

class ToDoApp:
    def __init__(self, storage):
        self.tasks = []
        self.storage = storage

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)
    
    def update_task(self, task_id, **kwargs):
        for task in self.tasks:
            if task.task_id == task_id:
                for key, value in kwargs.items():
                    if hasattr(task, key):
                        setattr(task, key, value)
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")
    
    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task.status == status]
        for task in filtered_tasks:
            print(task)

    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks saved successfully!")

    def load_tasks(self):
        self.tasks = self.storage.load()
        print("Tasks loaded successfully!")

class JSONStorage:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
    
    def save(self, tasks):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in tasks], file)
    
    def load(self):
        try:
            with open(self.filename, "r") as file:
                return [Task(**task) for task in json.load(file)]
        except FileNotFoundError:
            return []

class CSVStorage:
    def __init__(self, filename="tasks.csv"):
        self.filename = filename
    
    def save(self, tasks):
        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Task ID", "Title", "Description", "Due Date", "Status"])
            writer.writeheader()
            writer.writerows([task.to_dict() for task in tasks])
    
    def load(self):
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                return [Task(**row) for row in reader]
        except FileNotFoundError:
            return []

# Example usage
if __name__ == "__main__":
    storage = JSONStorage()  # Change to CSVStorage() for CSV format
    app = ToDoApp(storage)
    
    app.add_task(Task(101, "Finish Homework", "Complete math and science homework.", "2024-12-31", "Pending"))
    app.view_tasks()
    app.save_tasks()
    app.load_tasks()
