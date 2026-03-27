from ddgs import DDGS
from langchain.tools import tool,BaseTool
import os


@tool("search_web")
def search_web(query: str,max_results: int = 5) -> str:
    """Search the web for the given query and return a summary of the results.
    Args:
        query (str): The search query.
        max_results (int): The maximum number of results to return.
    Returns:
        str: A summary of the search results. yet to be summarized.
    """
    print("Searching the web for query:", query )
    with DDGS() as ddgs:
        results:list = ddgs.text(query, max_results=5)
        result = "\n".join([result["body"] for result in results if "body" in result])
        del results
    return result

from typing import TypedDict

class Task(TypedDict):
    title: str
    is_done: bool

tasks:list[Task] = []

if os.path.exists("./tasks.csv"):
    with open("./tasks.csv", "r") as f:
        data = f.read().strip().split("\n")
        if len(data)>1:
            for row in data:
                title, is_done = row.split(",")
                tasks.append(Task(title=title, is_done= is_done == "True"))
else:
    with open("./tasks.csv", "w") as f:
        pass


@tool("get_tasks")
def get_tasks():
    """get the task list from the file and return it."""
    return tasks

@tool("add_task")
def add_task(task: str):
    """add a new task to the task list and save it to the file."""
    new_task = Task(title=task, is_done=False)
    tasks.append(new_task)
    with open("./tasks.csv", "a") as f:
        f.write(f"{task},False\n")
    return f"Task '{task}' added successfully."

@tool("complete_task")
def complete_task(task_title: str):
    """get the task list, find the task with the given title, mark it as done, and save the updated list back to the file."""
    for task in tasks:
        if task["title"] == task_title:
            task["is_done"] = True
            with open("./tasks.csv", "w") as f:
                for t in tasks:
                    f.write(f"{t['title']},{t['is_done']}\n")
            return f"Task '{task_title}' marked as completed."
    return f"Task '{task_title}' not found."

@tool("delete_task")
def delete_task(task_title: str):
    """get the task list, find the task with the given title, remove it from the list, and save the updated list back to the file."""
    global tasks
    tasks = [task for task in tasks if task["title"] != task_title]
    with open("./tasks.csv", "w") as f:
        for t in tasks:
            f.write(f"{t['title']},{t['is_done']}\n")
    return f"Task '{task_title}' deleted successfully."


# all_tools:list[BaseTool] = [search_web]

all_tools:list[BaseTool] = [search_web, get_tasks, add_task, complete_task, delete_task]