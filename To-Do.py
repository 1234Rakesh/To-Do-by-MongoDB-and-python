
from pymongo import MongoClient

class TodoList:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['todo']
        self.collection = self.db['tasks']

    def add_task(self, task):
        self.collection.insert_one({'task': task})

    def update_task(self, old_task, new_task):
        self.collection.update_one({'task': old_task}, {'$set': {'task': new_task}})

    def delete_task(self, task):
        self.collection.delete_one({'task': task})

    def list_tasks(self):
        tasks = self.collection.find({})
        for task in tasks:
            print(task['task'])

def main():
    todo_list = TodoList()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            old_task = input("Enter the task to update: ")
            new_task = input("Enter the new task: ")
            todo_list.update_task(old_task, new_task)
        elif choice == '3':
            task = input("Enter the task to delete: ")
            todo_list.delete_task(task)
        elif choice == '4':
            print("\n===== TASKS =====")
            todo_list.list_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()