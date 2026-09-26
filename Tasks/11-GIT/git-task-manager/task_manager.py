import json
from pathlib import Path

TASKS_FILE = Path("tasks.json")


def load_tasks():
    if not TASKS_FILE.exists():
        return []

    with open(TASKS_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    priority = input("Enter priority (low/medium/high): ").strip().lower()

    if priority not in ["low", "medium", "high"]:
        print("Invalid priority.")
        return

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks")
    print("-" * 40)

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(
    f'{task["id"]}. {task["title"]} '
    f'- {task["priority"]} '
    f'- {status}'
)


def complete_task(tasks):
    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Please enter a valid task ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
            return

    print("Task not found.")


def delete_task(tasks):
    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Please enter a valid task ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully.")
            return

    print("Task not found.")




def show_summary(tasks):
    total = len(tasks)
    completed = sum(task["completed"] for task in tasks)
    pending = total - completed

    print("\nTask Summary")
    print("-" * 30)
    print(f"Total tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")




def main():
    tasks = load_tasks()

    while True:
        print("\n=== Git Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Task Summary")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            show_summary(tasks)
        elif choice == "6":
            print("Exiting the task manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()