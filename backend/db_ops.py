import os

db_con = None
db_name = "jarvis.db"


def init():
    if os.path.exists(db_name):
        return "Database already initialized."
    else:
        global db_con
        import sqlite3
        db_con = sqlite3.connect(db_name)
        cursor = db_con.cursor()
        cursor.execute(
            """CREATE TABLE tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0
            )"""
        )
        cursor.execute(
            """CREATE TABLE notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL
            )"""
        )
        cursor.execute(
            """CREATE TABLE reminders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                reminder_text TEXT NOT NULL,
                remind_at DATETIME NOT NULL
            )"""
        )
        db_con.commit()
        print("Database initialized successfully.")

init()
def get_db_connection():
    global db_con
    if db_con is None:
        import sqlite3
        db_con = sqlite3.connect(db_name)
        print("Database connection established.")
    return db_con

def close_db_connection():
    global db_con
    if db_con is not None:
        db_con.close()
        db_con = None
        print("Database connection closed.")


def get_all_tasks():
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("SELECT id, name, description, completed FROM tasks")
    rows = cursor.fetchall()
    tasks = []
    for row in rows:
        task = {
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "completed": bool(row[3])
        }
        tasks.append(task)
    close_db_connection()
    return tasks

def get_all_notes():
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("SELECT id, content FROM notes")
    rows = cursor.fetchall()
    notes = []
    for row in rows:
        note = {
            "id": row[0],
            "content": row[1]
        }
        notes.append(note)
    close_db_connection()
    return notes

def get_all_reminders():
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("SELECT id, reminder_text, remind_at FROM reminders")
    rows = cursor.fetchall()
    reminders = []
    for row in rows:
        reminder = {
            "id": row[0],
            "reminder_text": row[1],
            "remind_at": row[2]
        }
        reminders.append(reminder)
    close_db_connection()
    return reminders


def get_reminder_by_id(reminder_id: int):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("SELECT id, reminder_text, remind_at FROM reminders WHERE id=?", (reminder_id,))
    row = cursor.fetchone()
    if row:
        reminder = {
            "id": row[0],
            "reminder_text": row[1],
            "remind_at": row[2]
        }
        close_db_connection()
        return reminder
    else:
        close_db_connection()
        return None

def delete_task_by_id(task_id: int):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    con.commit()
    close_db_connection()
    return f"Task with id {task_id} deleted."

def update_task_completion(task_id: int, completed: bool):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("UPDATE tasks SET completed=? WHERE id=?", (int(completed), task_id))
    con.commit()
    close_db_connection()
    return f"Task with id {task_id} updated to completed={completed}."

def update_reminder_time(reminder_id: int, new_time: str):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("UPDATE reminders SET remind_at=? WHERE id=?", (new_time, reminder_id))
    con.commit()
    close_db_connection()
    return f"Reminder with id {reminder_id} updated to remind_at={new_time}."

def delete_reminder_by_id(reminder_id: int):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("DELETE FROM reminders WHERE id=?", (reminder_id,))
    con.commit()
    close_db_connection()
    return f"Reminder with id {reminder_id} deleted."

def delete_note_by_id(note_id: int):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("DELETE FROM notes WHERE id=?", (note_id,))
    con.commit()
    close_db_connection()
    return f"Note with id {note_id} deleted."


def add_task(name: str, description: str):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO tasks (name, description, completed) VALUES (?, ?, ?)",
        (name, description, 0)
    )
    con.commit()
    close_db_connection()
    

def get_task_by_id(task_id: int):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("SELECT id, name, description, completed FROM tasks WHERE id=?", (task_id,))
    row = cursor.fetchone()
    if row:
        task = {
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "completed": bool(row[3])
        }
        close_db_connection()
        return task
    else:
        close_db_connection()
        return None


def get_note_by_id(note_id: int):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("SELECT id, content FROM notes WHERE id=?", (note_id,))
    row = cursor.fetchone()
    if row:
        note = {
            "id": row[0],
            "content": row[1]
        }
        close_db_connection()
        return note
    else:
        close_db_connection()
        return None


def add_note(content: str):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO notes (content) VALUES (?)",
        (content,)
    )
    con.commit()
    note_id = cursor.lastrowid
    close_db_connection()
    return note_id

def add_reminder(reminder_text: str, remind_at: str):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO reminders (reminder_text, remind_at) VALUES (?, ?)",
        (reminder_text, remind_at)
    )
    con.commit()
    reminder_id = cursor.lastrowid
    close_db_connection()
    return reminder_id

def update_task_content(task_id: int, new_name: str, new_description: str):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("UPDATE tasks SET name=?, description=? WHERE id=?", (new_name, new_description, task_id))
    con.commit()
    close_db_connection()
    return f"Task with id {task_id} updated."

def update_note_content(note_id: int, new_content: str):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("UPDATE notes SET content=? WHERE id=?", (new_content, note_id))
    con.commit()
    close_db_connection()
    return f"Note with id {note_id} updated."

def exit_handler():
    close_db_connection()