from tasks import add_task, show_tasks, add_priority

tasks = []

print("# TASK MANAGER")

add_task(tasks, "Learn Git")
add_task(tasks, "Push project to GitHub")

show_tasks(tasks)

print("\nPriority Task:")
print(add_priority("Complete Git assignment", "HIGH"))