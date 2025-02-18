tasks = []

def create_task(description, priority="normal"):
    task = {"description": description, "priority": priority, "completed": False}
    tasks.append(task)
    return task

def update_task(index, description=None, priority=None, completed=None):
    if 0 <= index < len(tasks):
        if description is not None:
            tasks[index]["description"] = description
        if priority is not None:
            tasks[index]["priority"] = priority
        if completed is not None:
            tasks[index]["completed"] = completed
        return tasks[index]
    return None

def delete_task(index):
       if 0 <= index < len(tasks):
           return tasks.pop(index)
       return None