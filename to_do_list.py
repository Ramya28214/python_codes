class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def remove_task(self, task_index):
        try:
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task}' removed.")
        except IndexError:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
            task_index = int(input("Enter task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
