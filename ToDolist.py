# TodoList class that represents the to-do list


class TodoList:
    def __init__(self):
        self.tasks = []

# Function to add task

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added:", task)

#Function to remove task


    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed:", task)
        else:
            print("Task not found:", task)

# Function to show task

    def show_tasks(self):
        print("To-Do List:")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

# The main function provides a simple command-line menu for users to add tasks, 
# remove tasks, show tasks, or exit the program.



def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
