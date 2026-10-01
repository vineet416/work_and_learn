from tasks import add_task, show_tasks

tasks = []

print("# TASK MANAGER")

add_task(tasks, "Learn Git")
add_task(tasks, "Push project to GitHub")

show_tasks(tasks)