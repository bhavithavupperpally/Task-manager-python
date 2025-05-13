# task_manager.py

# Function to display all tasks
def display_tasks(tasks):
    print("\nYour tasks:")
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Function to add a new task
def add_task(tasks, task):
    tasks.append(task)
    print(f"'{task}' added!")

# Function to delete a task
def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"'{removed_task}' deleted!")
    else:
        print("Invalid task index!")

# Function to save tasks to a file
def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")
    print("Tasks saved to file.")

# Function to load tasks from a file
def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Main function to interact with the user
def main():
    tasks = load_tasks()
    
    while True:
        print("\nTask Manager")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Save and Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == '3':
            display_tasks(tasks)
            task_index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, task_index)
        elif choice == '4':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# Call main to run the program
if __name__ == "__main__":
    main()
          
