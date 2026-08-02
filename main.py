
# Define the empty task set
task_set = set()

# Limit the set to a maximum of 10 tasks
MAX_TASKS = 10 

# Take the user input for tasks
while len(task_set) < MAX_TASKS:
    task = input("Enter a task (or type 'done' to finish): ")
    if task.lower() == 'done':
        break
    elif task in task_set:
        print("Task already exists. Please enter a different task.")
    else:
        task_set.add(task)
        print(f"Task '{task}' added.")

# Prevent the user from adding more than 10 tasks
if len(task_set) == MAX_TASKS:
    print("You have reached the maximum number of tasks (10). No more tasks can be added.")

# Display final numbered list of tasks
print("\nFinal list of tasks:")
for idx, task in enumerate(task_set, start=1):
    print(f"{idx}. {task}")

# Allow user to choose a specific task to mark as completed by number
completed_task = input("\nEnter the number of the task you want to mark as completed: ")  

# Delete completed tasks by number 
try:
    completed_task_index = int(completed_task) - 1
    if 0 <= completed_task_index < len(task_set):
        task_to_remove = list(task_set)[completed_task_index]
        task_set.remove(task_to_remove)
        print(f"Task '{task_to_remove}' marked as completed and removed from the list.")
    else:
        print("Invalid task number. Please enter a valid number.")
except ValueError:
    print("Invalid input. Please enter a valid task number.")

# Display the updated list of tasks after marking a task as completed
print("\nUpdated list of tasks:")
for idx, task in enumerate(task_set, start=1):
    print(f"{idx}. {task}")

# Ask user if they want to add or delete more tasks or exit the program
while True:
    choice = input("\nDo you want to add or delete more tasks? (add/delete/exit): ").strip().lower()
    if choice == 'add':
        while len(task_set) < MAX_TASKS:
            task = input("Enter a task (or type 'done' to finish): ")
            if task.lower() == 'done':
                break
            elif task in task_set:
                print("Task already exists. Please enter a different task.")
            else:
                task_set.add(task)
                print(f"Task '{task}' added.")
        if len(task_set) == MAX_TASKS:
            print("You have reached the maximum number of tasks (10). No more tasks can be added.")
    elif choice == 'delete':
        completed_task = input("\nEnter the number of the task you want to delete: ")
        try:
            completed_task_index = int(completed_task) - 1
            if 0 <= completed_task_index < len(task_set):
                task_to_remove = list(task_set)[completed_task_index]
                task_set.remove(task_to_remove)
                print(f"Task '{task_to_remove}' deleted.")
            else:
                print("Invalid task number. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
    elif choice == 'exit':
        break
    else:
        print("Invalid choice. Please enter 'add', 'delete', or 'exit'.")

# Display the final list of tasks before exiting
print("\nFinal list of tasks before exiting:") 
for idx, task in enumerate(task_set, start=1):
    print(f"{idx}. {task}")

# Wait for the user to press Enter before exiting
print("\nPress Enter to exit.")
input()

