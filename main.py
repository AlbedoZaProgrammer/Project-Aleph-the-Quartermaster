import json
from pathlib import Path

MAX_TASKS = 50

# Display the current list of tasks
def display_tasks(tasks):
    print("\nCurrent list of tasks:")
    if not tasks:
        print("  (no tasks)")
        return
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

# Add tasks to the list, ensuring no duplicates and not exceeding MAX_TASKS
def add_tasks(tasks):
    while len(tasks) < MAX_TASKS:
        task = input("Enter a task (or type 'done' to finish): ").strip()
        if task.lower() == 'done':
            break
        elif not task:
            print("Task cannot be empty.")
        elif task in tasks:
            print("Task already exists. Please enter a different task.")
        else:
            tasks.append(task)
            print(f"Task '{task}' added.")
    if len(tasks) == MAX_TASKS:
        print(f"You have reached the maximum number of tasks ({MAX_TASKS}). No more tasks can be added.")

# Remove a task by its number, with error handling for invalid input   
def remove_task_by_number(tasks, prompt):
    if not tasks:
        print("The task list is empty. No tasks to remove.")
        return
    choice = input(prompt)
    try:
        index = int(choice) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Task '{removed}' removed.")
        else:
            print("Invalid task number. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Saves task list to a .json file
def save_tasks(tasks, filename="tasks.json"):
    """Save the task list to a JSON file."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=2, ensure_ascii=False)
        print(f"Tasks saved to {filename}.")
        return True
    except OSError as e:
        print(f"Error saving tasks to {filename}: {e}")
        return False

# Re-import task list from a .json file
def load_tasks(filename="tasks.json"):
    """Load the task list from a JSON file, validating its contents."""
    if not Path(filename).exists():
        print("No existing task file found. Starting with an empty task list.")
        return []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            tasks = json.load(file)
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}. Starting with an empty task list.")
        return []
    except OSError as e:
        print(f"Error loading tasks from {filename}: {e}")
        return []

    if not isinstance(tasks, list) or not all(isinstance(t, str) for t in tasks):
        print(f"{filename} did not contain a valid list of tasks. Starting with an empty task list.")
        return []

    print(f"Tasks loaded from {filename}.")
    return tasks[:MAX_TASKS]

# Main function to run the task management program
def main():
    tasks = []

    load_choice = input("Do you want to load existing tasks from a file? (yes/no): ").strip().lower()

    match load_choice:
        case "yes":
            tasks = load_tasks()
            display_tasks(tasks)
        case "no":
            print("Starting with an empty task list.")
        case _:
            print("Invalid input. Starting with an empty task list.")

    add_tasks(tasks)

    if not tasks:
        print("No tasks were added. Exiting the program.")
        return

    display_tasks(tasks)
    remove_task_by_number(tasks, "\nEnter the number of the task to mark as completed: ")
    display_tasks(tasks)

    while True:
        choice = input("\nDo you want to add or delete more tasks? (add/delete/exit): ").strip().lower()
        if choice == 'add':
            add_tasks(tasks)
            display_tasks(tasks)
        elif choice == 'delete':
            remove_task_by_number(tasks, "\nEnter the number of the task to delete: ")
            display_tasks(tasks)
        elif choice == 'exit':
            break
        else:
            print("Invalid choice. Please enter 'add', 'delete', or 'exit'.")

    print("\nFinal list of tasks before exiting:")
    display_tasks(tasks)

    save_choice = input("\nDo you want to save these tasks to a file? (yes/no): ").strip().lower()
    if save_choice == 'yes':
        save_tasks(tasks)

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()