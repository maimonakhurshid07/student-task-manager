# Student Task Manager - Day 1 Structure
tasks = []

def add_task(title, subject, due_date):
    task = {"title": title, "subject": subject, "due_date": due_date, "status": "Pending"}
    tasks.append(task)
    print(f"Task '{title}' added successfully!")

# Initial Test
add_task("AD Assignment", "BCS", "2026-09-20")
print(tasks)
