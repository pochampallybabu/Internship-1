import os

class TaskManager:
    def __init__(self, filename='tasks.txt'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the text file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.tasks = [line.strip() for line in file.readlines()]
            except Exception as e:
                print(f"Error loading tasks: {e}")

    def save_tasks(self):
        """Save tasks to the text file."""
        try:
            with open(self.filename, 'w') as file:
                for task in self.tasks:
                    file.write(task + '\n')
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def add_task(self, task):
        """Add a new task."""
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        """View all tasks."""
        if not self.tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def delete_task(self, task_index):
        """Delete a task by index."""
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            self.save_tasks()
            print(f"Deleted task: {removed_task}")
        else:
            print("Invalid task index.")

    def update_task(self, task_index, new_task):
        """Update a task by index."""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] = new_task
            self.save_tasks()
            print(f"Updated task: {new_task}")
        else:
            print("Invalid task index.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            task_manager.add_task(task)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            task_manager.view_tasks()
            task_index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            task_manager.update_task(task_index, new_task)
        elif choice == '4':
            task_manager.view_tasks()
            task_index = int(input("Enter the task number to delete: ")) - 1
            task_manager.delete_task(task_index)
        elif choice == '5':
            print("Exiting the Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
