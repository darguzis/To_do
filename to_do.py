# To Do program:


task_list = []
app_running = True
while app_running:

    print("1. Add task.")
    print("2. View tasks.")
    print("3. Remove task.")
    print("4. Exit.")
    choice = int(input("Choose an option (1-4):\n"))

# Add task:

    if choice == 1:
        task = input("Task: \n").lower()
        task_list.append(task)
        print(f"Added to your task list : '{task}'")
        print()

# View tasks:

    elif choice == 2:
        if task_list:
            print("Your tasks:")
            for i, task in enumerate(task_list, 1):
                print(f"{i}. {task}")
            print()
        else:
            print("Your task list is empty:")


# Remove task:

    elif choice == 3:
        print("Your tasks:")
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task}")
        print()
        print("1. Remove last task.")
        print("2. Remove task by position.")
        print("3. Clear list.")
        rem_choice = int(input("Choose an option (1-3):\n"))
        if rem_choice == 1:
            if task_list:
                task_list.pop()
                print("Last task removed.")
            else:
                print("Your task list is already empty.")

        if rem_choice == 2:
            try:
                rem_task = int(
                    input("Enter the number of the task you wish to remove: \n"))
                if 1 <= rem_task <= len(task_list):
                    removed = task_list.pop(rem_task - 1)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        if rem_choice == 3:
            task_list.clear()
            print("Task lisk has been cleared.")


# Exit app:

    elif choice == 4:
        print("Goodbye!")
        break


# Invalid option:

    else:
        print("Invalid option. Choose (1-4)")
