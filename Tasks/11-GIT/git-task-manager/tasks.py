def add_task(tasks, task):
    tasks.append(task)

def show_tasks(tasks):
    print("\nTasks:")
    for task in tasks:
        print(f"- {task}")

def add_priority(task, priority):
    return f"[{priority}] {task}"

def add_status(task, status):
    return f"{task} - Status: {status}"

def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
        print(f"Removed: {task}")