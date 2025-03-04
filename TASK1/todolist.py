import os
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list"""
        self.tasks.append(task)
        print(f"Task '{task}' added successfully!")

    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("\nYour To-Do List:")
            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")
    
    def remove_task(self, task_number):
        """Remove a task by number"""
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number!")

    def update_task(self, task_number, new_task):
        """Update a task with a new task"""
        if 0 < task_number <= len(self.tasks):
            old_task = self.tasks[task_number - 1]
            self.tasks[task_number - 1] = new_task
            print(f"Task '{old_task}' updated to '{new_task}'!")
        else:
            print("Invalid task number!")

# Function to display the menu
def display_menu():
    print("\n--- To-Do List Application ---")
    print("1. Add a new task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Update a task")
    print("5. Exit")

# Main function to run the program
def main():
    todo_list = TodoList()

    while True:
        display_menu()

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task to add: ")
            todo_list.add_task(task)

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == "3":
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                todo_list.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "4":
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to update: "))
                new_task = input("Enter the updated task: ")
                todo_list.update_task(task_number, new_task)
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "5":
            print("Exiting To-Do List Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()
