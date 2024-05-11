class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task, priority):
        self.tasks[task] = priority
        print(f"Task '{task}' added to the ToDo list with priority {priority}.")

    def update_task_priority(self, task, new_priority):
        if task in self.tasks:
            self.tasks[task] = new_priority
            print(f"Priority of task '{task}' updated to {new_priority}.")
        else:
            print(f"Task '{task}' not found in the ToDo list.")

    def remove_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
            print(f"Task '{task}' removed from the ToDo list.")
        else:
            print(f"Task '{task}' not found in the ToDo list.")

    def view_tasks(self):
        if self.tasks:
            print("Tasks in the ToDo list:")
            for task, priority in self.tasks.items():
                print(f"{task} - Priority: {priority}")
        else:
            print("No tasks in the ToDo list.")

# Example usage
if __name__ == "__main__":
    todo_list = ToDoList()
    
    while True:
        print("\n===== ToDo List Menu =====")
        print("1. Add Task")
        print("2. Update Task Priority")
        print("3. Remove Task")
        print("4. View Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            task = input("Enter task to add: ")
            priority = input("Enter priority for the task: ")
            todo_list.add_task(task, priority)
        elif choice == '2':
            task = input("Enter task to update priority: ")
            new_priority = input("Enter new priority: ")
            todo_list.update_task_priority(task, new_priority)
        elif choice == '3':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == '4':
            todo_list.view_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
