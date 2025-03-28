
def displaytasks(tasks):                               # Function for display all tasks
    if not tasks:
        print("No tasks to display..Please Add Some Task in the list.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def delet_task(tasks, taskindex):                     # Function for delete a task
    if 1 <= taskindex <= len(tasks):
        delet_task = tasks.pop(taskindex - 1)
        print(f"Task '{delet_task}' deleted from the To-do list.")
    else:
        print("Invalid task number, Please enter a valid task number.")

def atask(tasks, task):                              # Function for add a task
    tasks.append(task)
    print(f"Task '{task}' added Successfully in the To-do list.")

def mascomplete(tasks, taskindex):                   # Function for mark a task as complete
    try:
        tasks.pop(taskindex - 1)
        print(f"Task {taskindex} marked as complete and removed from the To-do list.")
    except IndexError:
        print("Invalid task number or You dont have any task in the To-do List.")




def todo():                                             # Main function to drive the app
    tasks = []                                          # List to store tasks
    while True:
        print("\n  **Welcome to To-Do List**")
        print("   Schedule Your day!")
        print("1. View All Tasks")
        print("2. Add Some Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit List")

        try:
            choice = int(input("Choose an option from 1 to 5: "))
            if choice == 1:
                displaytasks(tasks)
            elif choice == 2:
                task = input("Enter the task description: ")
                atask(tasks, task)
            elif choice == 3:
                taskindex = int(input("Enter task number to mark as complete: "))
                mascomplete(tasks, taskindex)
            elif choice == 4:
                taskindex = int(input("Enter task number you wanted to delete: "))
                delet_task(tasks, taskindex)
            elif choice == 5:
                print("Exiting the To-Do Lists.")
                break
            else:
                print("Invalid choice. Please select between 1-5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

                                                        # Run the to-do App
todo()