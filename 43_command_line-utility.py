# --------------------------
# Command Line utilities
# --------------------------

#Rules:-
"""
1. Use argparse for arguments (or click/typer for more advanced tools).
2. Keep functions separate (don’t mix parsing and logic).
3. Always add --help descriptions (so users know how to use it).
4. Use subcommands for different operations (like git add, git commit).
5. Make it executable with a shebang (#!/usr/bin/env python3) if needed.
6. Follow Unix rules: Print output, don’t pop up windows.
"""

#!/usr/bin/env python3
import argparse
import json
import os

FILE = "todo.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            try:
                data = json.load(f)
                return data
            except json.JSONDecodeError:  # If file is empty or broken
                return []
    return []




# Save tasks
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# Add task
def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")

# List tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

# Remove task
def remove_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Removed: {removed}")
    else:
        print("Invalid task number.")

# CLI Setup
parser = argparse.ArgumentParser(description="Simple TODO CLI")
subparsers = parser.add_subparsers(dest="command")

# Add command
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("task", type=str, help="Task description")

# List command
list_parser = subparsers.add_parser("list", help="List all tasks")

# Remove command
remove_parser = subparsers.add_parser("remove", help="Remove a task")
remove_parser.add_argument("index", type=int, help="Task number to remove")

args = parser.parse_args()

# Run based on command
if args.command == "add":
    add_task(args.task)
elif args.command == "list":
    list_tasks()
elif args.command == "remove":
    remove_task(args.index)
else:
    parser.print_help()
