from asyncio import tasks
import json
import os

task_file = "task.json"


def load_tasks():
    if os.path.exists(task_file):
        with open(task_file, 'r') as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(task_file, 'w') as f:
        json.dump(tasks, f, indent=4)


tasks = [{"task": "Buy groceries", "status": "pending"},
         {"task": "Clean the house", "status": "pending"},
         ]
save_tasks(tasks)
print("saved check tasks.json")


def add_task(task):
    tasks = load_tasks()      # Get current list
    tasks.append({"task": task, "done": False})  # Add new dict
    save_tasks(tasks)         # Persist
    print(f"Added: {task}")


add_task("Test add")
