"""Capstone template project for FCS Task 19 Compulsory task 1 and 2."""

# =====importing libraries===========
"""This is the section where you will import libraries"""
from datetime import date
import calendar

# ====Login Section====
"""Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
"""
# Fill dictionary with username and password pairs from user.txt
with open("user.txt", "r") as f:
    lines = f.readlines()
    login_data = {}
    for line in lines:
        key, value = line.strip().split(", ")
        login_data[key] = value

# Request username and password and compare against dictionary until true
while True:
    username = input("Please enter a username:")
    password = input("Please enter a password: ")
    if login_data.get(username) == password:
        break
    else:
        print(
            "Username or password failed. Please enter a valid username and password. "
        )

while True:
    if username == "admin":
        # presenting the menu to the user and
        # making sure that the user input is coneverted to lower case.
        menu = input(
            """Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - View my task
        s - Statistics
        e - Exit
        : """
        ).lower()
    else:
        # presenting the menu to the user and
        # making sure that the user input is coneverted to lower case.
        menu = input(
            """Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - View my task
        s - Statistics
        e - Exit
        : """
        ).lower()

    if menu == "r":
        """Add a new user to the user.txt file if admin
        - Request input of a new username, Request input of a new password, Request input of password confirmation, if confirmed -add them to the user.txt file,
        """
        if username == "admin":
            new_username = input("Please enter a username: ")
            new_password = input("Please enter a new password: ")
            password_conf = input("Please reenter the password to confirm: ")
            if new_password == password_conf:
                with open("user.txt", "a+") as f:
                    f.write("\n" + new_username + ", " + new_password)
                    print("New user registered.")
            else:
                print("Passwords don't match. Please try again")
        else:
            print("\n\nOnly admin can register new users.")
    elif menu == "a":
        """Allow a user to add a new task to task.txt file
        - Prompt a user a username, task title, description, due date and add the current date and "No" to task.txt
        """
        username = input(
            "Please enter the username of the person the task is assigned to: "
        )
        title = input("Please enter the task title: ")
        description = input("Please enter the task description: ")
        due_date = input("Please enter the task due date: ")
        assigned_date = date.today()
        assigned_date = (
            str(assigned_date.day)
            + " "
            + str(calendar.month_abbr[assigned_date.month])
            + " "
            + str(assigned_date.year)
        )
        with open("tasks.txt", "a+") as f:
            f.write(
                "\n"
                + username
                + ", "
                + title
                + ", "
                + description
                + ", "
                + due_date
                + ", "
                + assigned_date
                + ", "
                + "No"
            )

    elif menu == "va":
        """Read the task from task.txt file and print to the console
        - Read a line from the file, split comma and space, print the results"""

        with open("tasks.txt", "r") as f:
            lines = [line.rstrip() for line in f]
            for i in range(0, len(lines)):
                task = lines[i].strip().split(", ")
                print(
                    f"Task: \t\t {task[1]} \nAssigned to: \t {task[0]} \nDate assigned: \t {task[3]} \nDue date: \t {task[4]} \nTask Complete: \t {task[5]} \nTask Description: \n   {task[2]} \n\n"
                )

    elif menu == "vm":
        """Read the task from task.txt file and print to the console in the format of Output 2 presented in the L1T19 pdf
        - Read a line from the file, split comma and space, print if user matches username in file
        """
        with open("tasks.txt", "r") as f:
            lines = [line.rstrip() for line in f]
            for i in range(0, len(lines)):
                task = lines[i].strip().split(", ")
                if username == task[0]:
                    print(
                        f"Task: \t\t {task[1]} \nAssigned to: \t {task[0]} \nDate assigned: \t {task[3]} \nDue date: \t {task[4]} \nTask Complete: \t {task[5]} \nTask Description: \n   {task[2]} \n\n"
                    )

    elif username == "admin" and menu == "s":
        with open("user.txt", "r") as f:
            num_users = f.readlines()
        with open("tasks.txt", "r") as f:
            num_tasks = f.readlines()
        print(
            f"\n\nNumber of Users: \t {len(num_users)} \nNumber of Tasks: \t {len(num_tasks)}"
        )

    elif menu == "e":
        print("Goodbye!!!")
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
