import os
from datetime import datetime

class TodoList:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.txt"
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from file if it exists."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    # Split the line into components
                    parts = line.strip().split('|')
                    if len(parts) == 4:
                        task_id, task, status, date = parts
                        self.tasks.append({
                            'id': int(task_id),
                            'task': task,
                            'status': status,
                            'date': date
                        })

    def save_tasks(self):
        """Save tasks to file."""
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task['id']}|{task['task']}|{task['status']}|{task['date']}\n")

    def add_task(self, task_description):
        """Add a new task to the list."""
        task_id = len(self.tasks) + 1
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_task = {
            'id': task_id,
            'task': task_description,
            'status': 'Pending',
            'date': current_date
        }
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{task_description}' added successfully!")

    def view_tasks(self):
        """Display all tasks with their details."""
        if not self.tasks:
            print("No tasks found!")
            return
        
        print("\n=== Your To-Do List ===")
        print("ID  | Status  | Date                 | Task")
        print("-" * 60)
        for task in self.tasks:
            print(f"{task['id']:<3} | {task['status']:<7} | {task['date']} | {task['task']}")
        print("-" * 60)

    def mark_completed(self, task_id):
        """Mark a task as completed."""
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = 'Done'
                self.save_tasks()
                print(f"Task {task_id} marked as completed!")
                return
        print(f"Task with ID {task_id} not found!")

    def delete_task(self, task_id):
        """Delete a task from the list."""
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"Task {task_id} deleted successfully!")
                return
        print(f"Task with ID {task_id} not found!")

    def search_tasks(self, keyword):
        """Search for tasks containing the given keyword."""
        found_tasks = [task for task in self.tasks if keyword.lower() in task['task'].lower()]
        if found_tasks:
            print("\n=== Search Results ===")
            print("ID  | Status  | Date                 | Task")
            print("-" * 60)
            for task in found_tasks:
                print(f"{task['id']:<3} | {task['status']:<7} | {task['date']} | {task['task']}")
            print("-" * 60)
        else:
            print(f"No tasks found containing '{keyword}'")

def main():
    todo_list = TodoList()
    
    while True:
        print("\nSNJ To-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Search Tasks")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            task = input("Enter task description: ")
            todo_list.add_task(task)
        
        elif choice == '2':
            todo_list.view_tasks()
        
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))
            todo_list.mark_completed(task_id)
        
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
        
        elif choice == '5':
            keyword = input("Enter search keyword: ")
            todo_list.search_tasks(keyword)
        
        elif choice == '6':
            print("Thank you for using SNJ To-Do List Application!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()