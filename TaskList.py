
tasks = []

print("==== To-Do List ====")

while True:

    print()
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Exit")

    choice = input("Choose an option: ")


    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added!")


    elif choice == "2":

        if len(tasks) == 0:
            print("There are no tasks to remove.")

        else:
            print("===== Your Tasks =====")

            for number, task in enumerate(tasks, start=1):
                print(number, task)

            task_number = int(input("Which task would you like to remove? "))

            tasks.pop(task_number - 1)

            print("Task removed.")


    elif choice == "3":

        if len(tasks) == 0:
            print("You have no tasks.")

        else:
            print("===== Your Tasks =====")

            for number, task in enumerate(tasks, start=1):
                print(number, task)


    elif choice == "4":
        break

    else:
        print("Invalid choice. Choose 1-4.")




