from models import db, Task
import uuid

# Create a new task
def create_task(name):
    task = Task(id=str(uuid.uuid4()), name=name)
    db.session.add(task)
    db.session.commit()
    return task

# List all tasks
def list_tasks():
    return Task.query.all()

# Get details of a specific task
def get_task(task_id):
    return Task.query.get(task_id)

# Delete a task
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return task
