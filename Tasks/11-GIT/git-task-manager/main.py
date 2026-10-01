from tasks import add_task, show_tasks, add_priority, remove_task

tasks = []

print("# TASK MANAGER")

add_task(tasks, "Learn Git")
add_task(tasks, "Push project to GitHub")

show_tasks(tasks)

print("\nPriority Task:")
print(add_priority("Complete Git assignment", "HIGH"))

remove_task(tasks, "Learn Git")

print("\nUpdated Tasks:")
show_tasks(tasks)