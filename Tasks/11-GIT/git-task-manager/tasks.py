def add_task(tasks, task):
    tasks.append(task)

def show_tasks(tasks):
    print("\nTasks:")
    for task in tasks:
        print(f"- {task}")

def add_priority(task, priority):
    return f"[{priority}] {task}"