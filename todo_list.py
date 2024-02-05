import os

class TodoList:
    def __init__(self, file_path="tasks.txt"):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task.strip()}")

    def add_task(self, new_task):
        self.tasks.append(new_task)
        print("Task added successfully.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task '{deleted_task.strip()}' deleted successfully.")
        else:
            print("Invalid task index.")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{completed_task.strip()}' marked as complete.")
        else:
            print("Invalid task index.")

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            for task in self.tasks:
                file.write(task)

    def load_tasks(self):
        tasks = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                tasks = file.readlines()
        return tasks

    def main_menu(self):
        while True:
            print("\nTodo List Menu:")
            print("1. Display Tasks")
            print("2. Add Task")
            print("3. Delete Task")
            print("4. Complete Task")
            print("5. Save and Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.display_tasks()
            elif choice == "2":
                new_task = input("Enter the new task: ")
                self.add_task(new_task + "\n")
            elif choice == "3":
                task_index = int(input("Enter the task index to delete: "))
                self.delete_task(task_index)
            elif choice == "4":
                task_index = int(input("Enter the task index to mark as complete: "))
                self.complete_task(task_index)
            elif choice == "5":
                self.save_tasks()
                print("Tasks saved. Exiting.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.main_menu()
