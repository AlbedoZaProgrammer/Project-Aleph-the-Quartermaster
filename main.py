
MAX_TASKS = 10

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

# Main function to run the task management program
def main():
    tasks = []

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

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()