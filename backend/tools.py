from langchain.tools import tool,BaseTool
from db_ops import get_all_tasks, add_task, get_reminder_by_id, delete_task_by_id, update_task_completion, update_reminder_time, delete_reminder_by_id, delete_note_by_id, exit_handler,get_task_by_id,get_all_reminders,get_all_notes,update_note_content,get_note_by_id,add_reminder,add_note
from ddgs.ddgs import DDGS
import os

@tool
def search_web(query: str) -> str:
    """Search the web for the given query and return a summary of the results.
    Args:
        query (str): The search query.
    Returns:
        str: A summary of the search results. yet to be summarized.
    """
    print("Searching the web for query:", query )
    with DDGS() as ddgs:
        results:list = ddgs.text(query, max_results=5)
        result = "\n".join([result["body"] for result in results if "body" in result])
        del results
    return result


@tool
def get_current_tasks() -> str:
    """Retrieve all current tasks from the database.
    Returns:
        str: A string representation of all current tasks.
    """
    print("Retrieving all current tasks from the database.")
    tasks = get_all_tasks()
    return str(tasks)


@tool
def get_task(task_id: int) -> str:
    """Retrieve a task by its ID.
    Args:
        task_id (int): The ID of the task.
    Returns:
        str: A string representation of the task."""
    print(f"Retrieving task with id: {task_id} from the database.")
    task = get_task_by_id(task_id)
    if task:
        return str(task)
    else:
        return f"No task found with id: {task_id}"

@tool
def get_current_reminders() -> str:
    """Retrieve all reminders from the database.
    Returns:
        str: A string representation of all reminders.
    """
    print("Retrieving all current reminders from the database.")
    reminders = get_all_reminders()
    return str(reminders)

@tool
def get_current_notes() -> str:
    """Retrieve all notes from the database.
    Returns:
        str: A string representation of all notes.
    """
    print("Retrieving all current notes from the database.")
    notes = get_all_notes()
    return str(notes)

@tool
def update_note(note_id: int, new_content: str) -> str:
    """Update the content of a note.
    Args:
        note_id (int): The ID of the note to update.
        new_content (str): The new content for the note.
    Returns:
        str: Confirmation message."""
    print(f"Updating note with id: {note_id} with new content.{new_content}")
    return update_note_content(note_id, new_content)

@tool
def get_note(note_id: int) -> str:
    """Retrieve a note by its ID.
    Args:
        note_id (int): The ID of the note.
    Returns:
        str: A string representation of the note."""
    print(f"Retrieving note with id: {note_id} from the database.")
    note = get_note_by_id(note_id)
    if note:
        return str(note)
    else:
        return f"No note found with id: {note_id}"



@tool
def add_new_task(name: str, description: str) -> str:
    """Add a new task to the database.
    Args:
        name (str): The name of the task.
        description (str): The description of the task.
    Returns:
        str: Confirmation message with the new task ID."""
    print(f"Adding new task with name: {name} and description: {description}")
    task_id = add_task(name, description)
    return f"Task added with id: {task_id}"

@tool
def get_reminder(reminder_id: int) -> str:
    """Retrieve a reminder by its ID.
    Args:
        reminder_id (int): The ID of the reminder.
    Returns:
        str: A string representation of the reminder."""
    print(f"Retrieving reminder with id: {reminder_id} from the database.")
    reminder = get_reminder_by_id(reminder_id)
    if reminder:
        return str(reminder)
    else:
        return f"No reminder found with id: {reminder_id}"

@tool
def delete_task(task_id: int) -> str:
    """Delete a task by its ID.
    Args:
        task_id (int): The ID of the task to delete.
    Returns:
        str: Confirmation message."""
    print(f"Deleting task with id: {task_id} from the database.")
    return delete_task_by_id(task_id)

@tool
def update_task(task_id: int, completed: bool) -> str:
    """Update the completion status of a task.
    Args:
        task_id (int): The ID of the task to update.
        completed (bool): The new completion status.
    Returns:
        str: Confirmation message."""
    print(f"Updating task with id: {task_id} to completed status: {completed}")
    return update_task_completion(task_id, completed)

@tool
def update_reminder(reminder_id: int, new_time: str) -> str:
    """Update the reminder time of a reminder.
    Args:
        reminder_id (int): The ID of the reminder to update.
        new_time (str): The new reminder time in ISO format.
    Returns:
        str: Confirmation message."""
    print(f"Updating reminder with id: {reminder_id} to new time: {new_time}")
    return update_reminder_time(reminder_id, new_time)

@tool
def delete_reminder(reminder_id: int) -> str:
    """Delete a reminder by its ID.
    Args:
        reminder_id (int): The ID of the reminder to delete.
    Returns:
        str: Confirmation message."""
    print(f"Deleting reminder with id: {reminder_id} from the database.")
    return delete_reminder_by_id(reminder_id)

@tool
def delete_note(note_id: int) -> str:
    """Delete a note by its ID.
    Args:
        note_id (int): The ID of the note to delete.
    Returns:
        str: Confirmation message."""
    print(f"Deleting note with id: {note_id} from the database.")
    return delete_note_by_id(note_id)



@tool
def exit_program() -> str:
    """Exit the program gracefully.
    Returns:
        str: Confirmation message.
    """
    print("Exiting the program gracefully.")
    exit_handler()
    os._exit(0)
    return "Program exited."

@tool
def add_new_reminder(reminder_text: str, remind_at: str) -> str:
    """Add a new reminder to the database.
    Args:
        reminder_text (str): The text of the reminder.
        remind_at (str): The time to remind in ISO format.
    Returns:
        str: Confirmation message with the new reminder ID."""
    print(f"Adding new reminder with text: {reminder_text} at time: {remind_at}")

    reminder_id = add_reminder(reminder_text, remind_at)
    return f"Reminder added with id: {reminder_id}"

@tool
def add_new_note(content: str) -> str:
    """Add a new note to the database.
    Args:
        content (str): The content of the note.
    Returns:
        str: Confirmation message with the new note ID."""
    print(f"Adding new note with content: {content}")

    note_id = add_note(content)
    return f"Note added with id: {note_id}"

all_tools:list[BaseTool] = [
    search_web,
    get_current_tasks,
    get_task,
    update_task,
    add_new_task,
    delete_task,
    get_current_reminders,
    get_reminder,
    update_reminder,
    delete_reminder,
    add_new_reminder,
    get_current_notes,
    get_note,
    update_note,
    delete_note,
    add_new_note,
    exit_program
]