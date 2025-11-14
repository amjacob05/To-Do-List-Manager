
# MSE121 Project: To-Do List Manager
# Purpose: Manage a simple to-do list with add/remove/mark-done check

def load_tasks(filename):
    tasks=[]
    try:
        infile=open(filename,"r")
        for line in infile:
            line=line.strip()
            if line=="":
                continue
            parts=line.split("|")
            name=parts[0]
            done_string=parts[1]
            if done_string == "True":
                done = True
            else:
                done = False
            task = {"name": name, "done": done}
            tasks.append(task)
        return tasks

    except FileNotFoundError:
        return []

        

            
            
    pass  


def save_tasks():
    """
    Saves the list of task dictionaries back to the text file.
    Overwrites to the file each time.
    """
    pass


def add_task():
    """
    Adds a new task dictionary to the tasks list.
    """
    pass


def remove_task():
    """
    Remove a task at the given index.
    If index invalid, print an error message.
    """
    pass


def mark_done():
    """
    Mark a task as completed.
    If already done or invalid index, handle code
    """
    pass


def list_tasks():
    """
    Return a formatted string showing each task with its status.
    Example output:
    1. [ ] Buy milk
    2. [x] Finish homework
    """
    pass


def menu_loop():
    """
    The main user interface loop.
    Show menu options, call other functions, save before exit.
    """
    pass

if __name__ == "__main__":
    
    pass



