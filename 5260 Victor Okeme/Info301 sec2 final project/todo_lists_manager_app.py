import os

TODO_FILE = "todos.txt"

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip().split("|") for line in f.readlines()]

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        for todo in todos:
            f.write(f"{todo[0]}|{todo[1]}\n")

def add_todo(task):
    todos = load_todos()
    todos.append([task, "incomplete"])
    save_todos(todos)
    print(f"Task '{task}' added successfully!")

def view_todos():
    todos = load_todos()
    if not todos:
        print("No tasks found.")
        return
    for i, todo in enumerate(todos, 1):
        status = "✓" if todo[1] == "complete" else " "
        print(f"{i}. [{status}] {todo[0]}")

def complete_todo(index):
    todos = load_todos()
    if 1 <= index <= len(todos):
        todos[index-1][1] = "complete"
        save_todos(todos)
        print(f"Task '{todos[index-1][0]}' marked as complete!")
    else:
        print("Invalid task number.")

def delete_todo(index):
    todos = load_todos()
    if 1 <= index <= len(todos):
        deleted_task = todos.pop(index-1)
        save_todos(todos)
        print(f"Task '{deleted_task[0]}' deleted successfully!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n--- Todo App ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            task = input("Enter the task: ")
            add_todo(task)
        elif choice == "2":
            view_todos()
        elif choice == "3":
            view_todos()
            index = int(input("Enter the task number to mark as complete: "))
            complete_todo(index)
        elif choice == "4":
            view_todos()
            index = int(input("Enter the task number to delete: "))
            delete_todo(index)
        elif choice == "5":
            print("Thank you for using the Todo App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()