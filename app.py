import time
import task
import pickle

def save():
    with open("tasks_database.db", "wb") as f:
        pickle.dump(task.tasks, f)

def load():
    try:
        with open("tasks_database.db", "rb") as f:
            task.tasks = pickle.load(f)
    except:
        return

def add_task(name, description):
    task.Task(name, description)
    save()

def remove_task(id):    
    for task_ in task.tasks:
        if task_.id == id:
            task_.remove()

    save()

def one():
    print("\n" + "-"*50)

    print("\nTasks:\n")

    if task.tasks:
        for task_ in task.tasks:
            print("{}) Name: {}, Description: {}".format(task_.id, task_.name, task_.description))
    else:
        print("No Current Tasks")

    print("\n" + "-"*20)
    print("1) Remove Task")
    print("2) Remove All Tasks")
    print("3) Back")
    print("\n" + "-"*20)
    
    try:
        view_choice = int(input("\nChoice: "))

        if view_choice == 1:
            id_choice = int(input("\nNumber: "))

            yn = input(f"\nAre you sure you want to delete {task.tasks[id_choice-1].name}?\n(y/n): ")

            if yn.lower() == "y" or yn.lower() == "yes":
                remove_task(id_choice)

            one()
        elif view_choice == 2:
            yn = input("\nAre you sure you want to delete all tasks?\n(y/n): ")

            if yn.lower() == "y" or yn.lower() == "yes":
                for i in range(len(task.tasks)):
                    remove_task(1)

            one()
    except:
        print("Please try again!")
        one()

def two():
    print("\n" +  "-"*50)

    name = input("\nEnter the name of the task: ")
    description = input("Enter the description of the task: ")

    if not name or not description:
        print("You don't have an input on name/description, Please try again!")
        two()

    add_task(name, description)

    print(f"\nNew Task Created:\nName: {name}\nDescription: {description}\n")

    time.sleep(3)

load()

print("Todo List:\n")

while True:
    print("_"*20)
    print("1) View Tasks")
    print("2) Add Task")
    print("3) Quit")
    print("_"*20)

    try:
        menu_input = int(input("\nChoice: "))

        if menu_input == 1:
            one()
        elif menu_input == 2:
            two()
        elif menu_input == 3:
            break
    except:
        print("Please Try Again!")

"""Made by TheLittleBro122"""