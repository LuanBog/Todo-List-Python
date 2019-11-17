import time
import task

def add_task(name, description):
    task.Task(name, description)

def remove_task(id):    
    for task_ in task.tasks:
        if task_.id == id:
            task_.remove()

def one():
    print("\n", "-"*50)

    print("\nTasks:\n")

    for task_ in task.tasks:
        print("{}) Name: {}, Description: {}".format(task_.id, task_.name, task_.description))

    print("\n", "-"*20)
    print("1) Remove Task")
    print("2) Back")
    print("\n", "-"*20)
        
    view_choice = int(input("\nChoice: "))

    if view_choice == 1:
        id_choice = int(input("\nNumber: "))

        yn = input(f"\nAre you sure you want to delete {task.tasks[id_choice-1].name}?\n(y/n): ")

        if yn.lower() == "y" or yn.lower() == "yes":
            remove_task(id_choice)

        one()

def two():
    print("\n", "-"*50)

    name = input("\nEnter the name of the task: ")
    description = input("Enter the description of the task: ")

    add_task(name, description)

    print(f"\nNew Task Created:\nName: {name}\nDescription: {description}\n")

    time.sleep(5)

print("Todo List:\n")

add_task("####", "########")
add_task("dwalkdmwa", "ndwkjadnwajknda")
add_task("156165156 156 1561", "26561651")
add_task("@##!#@!$!#", "@#!&*(#!&(*@))")

while True:
    print("_"*20)
    print("1) View Tasks")
    print("2) Add Task")
    print("3) Quit")
    print("_"*20)

    menu_input = int(input("\nChoice: "))

    if menu_input == 1:
        one()
    elif menu_input == 2:
        two()
    elif menu_input == 3:
        break

#TODO: Try creating a Task Class instead, Saving tasks to a database with pickle