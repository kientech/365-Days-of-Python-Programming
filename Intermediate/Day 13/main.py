# Coding With Kien - 365 Days of Python Programming
# Intermediate - Day 13

# Command-Line To-Do List Application
import argparse
import json
import os

TODO_FILE = "todolist.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(task_description):
    tasks = load_tasks()
    tasks.append({"description": task_description, "status": "pending"})
    save_tasks(tasks)
    print(f"Added task: '{task_description}'")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks):
        print(f"{i + 1}. [{task['status']}] {task['description']}")

def complete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['status'] = 'completed'
        save_tasks(tasks)
        print(f"Completed task {task_number}")
    else:
        print("Invalid task number.")

def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Deleted task: '{removed['description']}'")
    else:
        print("Invalid task number.")

def main():
    parser = argparse.ArgumentParser(description="A simple command-line to-do list application.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 'add' command
    parser_add = subparsers.add_parser("add", help="Add a new task.")
    parser_add.add_argument("description", type=str, help="The description of the task.")

    # 'list' command
    subparsers.add_parser("list", help="List all tasks.")

    # 'complete' command
    parser_complete = subparsers.add_parser("complete", help="Mark a task as completed.")
    parser_complete.add_argument("task_number", type=int, help="The number of the task to complete.")

    # 'delete' command
    parser_delete = subparsers.add_parser("delete", help="Delete a task.")
    parser_delete.add_argument("task_number", type=int, help="The number of the task to delete.")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "complete":
        complete_task(args.task_number)
    elif args.command == "delete":
        delete_task(args.task_number)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

# Example Usage from the terminal:
# python main.py add "Buy milk"
# python main.py add "Read a book"
# python main.py list
# python main.py complete 2
# python main.py delete 1
# python main.py list 