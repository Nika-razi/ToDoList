
    # Task list initialization
Tasks = []

# Function to show the menu
def menu():
    print('\nTask list menu')
    print('1. Add a task')
    print('2. Remove a task')
    print('3. Show all tasks')
    print('4. Exit')


# Function to add a task
def add():
    task = input('Enter the task you want to add: ')
    if task.strip() == "":  # If user didn't enter anything
        print("Please enter a task.")
    else:
        Tasks.append(task)
        print(f"Task '{task}' has been added.")
        
        # Save task to the file
        with open('tasks.txt', 'a') as file:
            file.write(task + '\n')

    return_to_menu()

# Function to show all tasks
def show():
    if not Tasks:
        print('The task list is empty.')
    else:
        print('\nYour tasks:')
        for index, task in enumerate(Tasks, start=1):
            print(f"{index}- {task}")
    
    return_to_menu()


# Function to delete tasks
def delete():
    if not Tasks:
        print('No tasks available to delete.')
    else:
        show()
        task_numbers = input("Enter task numbers to delete (comma-separated) or type 'back' to return to the menu: ").strip()
        if task_numbers.lower() == 'back':
            return_to_menu()
            return

        task_indices = task_numbers.split(',')
        valid_indices = []
        for num in task_indices:
            if num.isdigit():
                index = int(num)
                if 1 <= index <= len(Tasks):
                    valid_indices.append(index)
                else:
                    print(f"Invalid task number: {num}")
            else:
                print(f"Invalid input: {num}")
        
        if valid_indices:
            for index in sorted(valid_indices, reverse=True):
                removed_task = Tasks.pop(index - 1)
                print(f"Task '{removed_task}' has been deleted.")
            
            # Save updated tasks to the file
            with open('tasks.txt', 'w') as file:
                for task in Tasks:
                    file.write(task + '\n')
        else:
            print("No valid tasks were deleted.")
    
    return_to_menu()


# Function to return to the menu
def return_to_menu():
    input("Press Enter to return to the main menu...")

# Function to load tasks from file
def load_task():
    try:
        with open('tasks.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Main function to control the menu and choices
def main():
    global Tasks
    Tasks = load_task()
    
    while True:
        menu()
        choice = input("Please enter a number from one to four: ").strip()

        if choice == '1':
            add()
        elif choice == '2':
            delete()
        elif choice == '3':
            show()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
                    
if __name__ == "__main__":
    main()

