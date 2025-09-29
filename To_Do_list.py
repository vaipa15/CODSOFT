todo_list = []

def show_list():
    print("Your To-Do List:")
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)

def delete_task():
    show_list()
    idx = int(input("Enter the number of the task to delete: ")) - 1
    if 0 <= idx < len(todo_list):
        todo_list.pop(idx)
    else:
        print("Invalid number.")

while True:
    print("1. Add Task \n 2. Delete Task \n 3. Show List \n 4. Exit")
    choice = input("Select an option: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        delete_task()
    elif choice == '3':
        show_list()
    elif choice == '4':
        break
    else:
        print("Invalid choice")
