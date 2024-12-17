import os

tasks = []

def show_menu():
    print("\n--- To-Do List Application ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_no < len(tasks):
            removed = tasks.pop(task_no)
            print(f"Task '{removed}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
