# task-scheduler-py

Python Task Scheduler:

This Python script is a simple task scheduler that allows users to add, view, and delete tasks based on specific dates and times. Additionally, it provides reminders for tasks due at the current time.

Features:
Add tasks with names and specific scheduled times (in YYYY-MM-DD HH:MM format)
View the list of scheduled tasks
Delete tasks from the list
Check reminders for tasks due at the current time

Usage: Prerequisites:
Python 3.x installed

How to Use:
Run the task_scheduler.py file.
Choose options from the menu to add tasks, view tasks, delete tasks, check reminders, or exit.

Notes:
Use the menu options (1-5) to navigate and perform various actions.
The script uses the datetime module for task scheduling.
Reminders are shown using the win10toast library to display Windows 10 toast notifications.

Code Details:
The task_scheduler.py Python script contains functions for adding, displaying, and deleting tasks. It utilizes the datetime module to handle task scheduling and win10toast for displaying reminders through toast notifications on Windows systems.

Disclaimer:
This script is developed for educational purposes as a simple demonstration of task scheduling using Python and should not be used for critical or production-level task management.
