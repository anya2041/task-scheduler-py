import datetime
from win10toast import ToastNotifier

tasks = []
toaster = ToastNotifier()

def add_task():
    task_name = input("Enter task name: ")
    task_time = input("Enter task time (YYYY-MM-DD HH:MM): ")

    try:
        task_time = datetime.datetime.strptime(task_time, "%Y-%m-%d %H:%M")
        tasks.append((task_name, task_time))
        print("Task added successfully!")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD HH:MM.")

def show_tasks():
    if not tasks:
        print("No tasks scheduled.")
    else:
        print("Scheduled Tasks:")
        for idx, (name, time) in enumerate(tasks, start=1):
            print(f"{idx}. {name} - {time.strftime('%Y-%m-%d %H:%M')}")

def delete_task():
    show_tasks()
    if not tasks:
        return
    
    try:
        idx = int(input("Enter the index of the task to delete: "))
        if 1 <= idx <= len(tasks):
            del tasks[idx - 1]
            print("Task deleted successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index number.")

def check_reminders():
    current_time = datetime.datetime.now()
    
    if tasks:
        for task_name, task_time in tasks:
            if current_time > task_time:
                print(f"Reminder: {task_name} is due now!")
                toaster.show_toast("Task Reminder", f"Task: {task_name} is due now!", duration=10)

while True:
    print("\n=== Task Scheduler Menu ===")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Check Reminders")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        check_reminders()
    elif choice == '5':
        print("Exiting Task Scheduler. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
