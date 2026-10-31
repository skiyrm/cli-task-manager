import json
import os

FILENAME = "tasks.json"

def load_tasks():
    """Load tasks from JSON file if it exists, otherwise return an empty list."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save the current list of tasks to JSON file."""
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found! Your list is empty.")
        return

    print("\n--- YOUR TASK LIST ---")
    for index, task in enumerate(tasks, start=1):
        status = "[X]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['title']}")

def add_task(tasks):
    title = input("\nEnter task description: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        print(f"Added: '{title}'")
    else:
        print("Task description cannot be empty!")

def mark_completed(tasks):
    display_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("\nEnter task number to mark completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            save_tasks(tasks)
            print("Task updated!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    display_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("\nEnter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted: '{removed['title']}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n====================")
        print("  CLI TASK MANAGER  ")
        print("====================")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Pick a number between 1 and 5.")

if __name__ == "__main__":
    main()
