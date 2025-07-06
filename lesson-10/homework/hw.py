from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = False  # False = Incomplete, True = Complete

    def mark_complete(self):
        self.status = True

    def __str__(self):
        status = "✅ Completed" if self.status else "❌ Incomplete"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {status}"

from task import Task

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            return True
        return False

    def list_all_tasks(self):
        return self.tasks

    def list_incomplete_tasks(self):
        return [task for task in self.tasks if not task.status]

from todo_list import ToDoList
from datetime import datetime

def display_menu():
    print("\n=== ToDo List Menu ===")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. List All Tasks")
    print("4. List Incomplete Tasks")
    print("5. Exit")

def main():
    todo = ToDoList()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Task Title: ")
            description = input("Task Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            todo.add_task(title, description, due_date)
            print("✅ Task added!")

        elif choice == "2":
            for i, task in enumerate(todo.list_all_tasks()):
                print(f"{i}. {task.title} - {'Completed' if task.status else 'Incomplete'}")
            try:
                index = int(input("Enter task number to mark as complete: "))
                if todo.mark_task_complete(index):
                    print("✅ Task marked as complete.")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "3":
            print("\n📋 All Tasks:")
            for task in todo.list_all_tasks():
                print(task)
                print("-" * 40)

        elif choice == "4":
            print("\n📋 Incomplete Tasks:")
            for task in todo.list_incomplete_tasks():
                print(task)
                print("-" * 40)

        elif choice == "5":
            print("👋 Exiting ToDo List. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

=== ToDo List Menu ===
1. Add Task
2. Mark Task as Complete
3. List All Tasks
4. List Incomplete Tasks
5. Exit
Enter your choice: 1
Task Title: Homework
Task Description: Finish math homework
Due Date (YYYY-MM-DD): 2025-07-07
 Task added!

from datetime import datetime

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()

    def edit(self, new_title, new_content):
        self.title = new_title
        self.content = new_content

    def __str__(self):
        return (f"Title: {self.title}\nAuthor: {self.author}\nDate: {self.created_at.strftime('%Y-%m-%d %H:%M')}\n"
                f"Content:\n{self.content}")

from post import Post

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, title, content, author):
        self.posts.append(Post(title, content, author))

    def list_all_posts(self):
        return self.posts

    def get_posts_by_author(self, author):
        return [post for post in self.posts if post.author.lower() == author.lower()]

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            del self.posts[index]
            return True
        return False

    def edit_post(self, index, new_title, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].edit(new_title, new_content)
            return True
        return False

    def get_latest_posts(self, count=5):
        return sorted(self.posts, key=lambda p: p.created_at, reverse=True)[:count]


from blog import Blog

def display_menu():
    print("\n=== Simple Blog Menu ===")
    print("1. Add Post")
    print("2. List All Posts")
    print("3. Show Posts by Author")
    print("4. Delete a Post")
    print("5. Edit a Post")
    print("6. Show Latest Posts")
    print("7. Exit")

def main():
    blog = Blog()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content:\n")
            author = input("Author: ")
            blog.add_post(title, content, author)
            print("✅ Post added!")

        elif choice == "2":
            print("\n📃 All Posts:")
            for i, post in enumerate(blog.list_all_posts()):
                print(f"\nPost #{i}")
                print(post)
                print("-" * 40)

        elif choice == "3":
            author = input("Enter author's name: ")
            posts = blog.get_posts_by_author(author)
            if posts:
                print(f"\n🖊 Posts by {author}:")
                for post in posts:
                    print(post)
                    print("-" * 40)
            else:
                print("❌ No posts by that author.")

        elif choice == "4":
            for i, post in enumerate(blog.list_all_posts()):
                print(f"{i}. {post.title} by {post.author}")
            try:
                index = int(input("Enter post number to delete: "))
                if blog.delete_post(index):
                    print("🗑️ Post deleted.")
                else:
                    print("❌ Invalid index.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "5":
            for i, post in enumerate(blog.list_all_posts()):
                print(f"{i}. {post.title} by {post.author}")
            try:
                index = int(input("Enter post number to edit: "))
                new_title = input("New Title: ")
                new_content = input("New Content:\n")
                if blog.edit_post(index, new_title, new_content):
                    print("✏️ Post updated.")
                else:
                    print("❌ Invalid index.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "6":
            print("\n🕒 Latest Posts:")
            for post in blog.get_latest_posts():
                print(post)
                print("-" * 40)

        elif choice == "7":
            print("👋 Exiting Blog System. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()


=== Simple Blog Menu ===
1. Add Post
2. List All Posts
3. Show Posts by Author
4. Delete a Post
5. Edit a Post
6. Show Latest Posts
7. Exit
Enter your choice: 1
Title: My First Post
Content:
This is my first blog post.
Author: Alice
 Post added!

class Account:
    def __init__(self, acc_number, holder_name, balance=0.0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def transfer(self, target_account, amount):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False

    def __str__(self):
        return (f"Account Number: {self.acc_number}\n"
                f"Holder Name: {self.holder_name}\n"
                f"Balance: ${self.balance:.2f}")


from account import Account

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, acc_number, holder_name, balance=0.0):
        if self.get_account(acc_number) is None:
            account = Account(acc_number, holder_name, balance)
            self.accounts.append(account)
            return True
        return False  # Account number already exists

    def get_account(self, acc_number):
        for acc in self.accounts:
            if acc.acc_number == acc_number:
                return acc
        return None

    def deposit(self, acc_number, amount):
        account = self.get_account(acc_number)
        if account:
            return account.deposit(amount)
        return False

    def withdraw(self, acc_number, amount):
        account = self.get_account(acc_number)
        if account:
            return account.withdraw(amount)
        return False

    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)
        if sender and receiver:
            return sender.transfer(receiver, amount)
        return False

    def check_balance(self, acc_number):
        account = self.get_account(acc_number)
        if account:
            return account.balance
        return None

    def display_account_details(self, acc_number):
        account = self.get_account(acc_number)
        if account:
            return str(account)
        return "Account not found."


from bank import Bank

def display_menu():
    print("\n=== Simple Banking System ===")
    print("1. Add Account")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Transfer Money")
    print("6. Display Account Details")
    print("7. Exit")

def main():
    bank = Bank()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            acc_number = input("Account Number: ")
            holder_name = input("Holder Name: ")
            try:
                balance = float(input("Initial Balance: "))
                if bank.add_account(acc_number, holder_name, balance):
                    print("✅ Account added successfully!")
                else:
                    print("❌ Account number already exists.")
            except ValueError:
                print("❌ Invalid balance input.")

        elif choice == "2":
            acc_number = input("Enter Account Number: ")
            balance = bank.check_balance(acc_number)
            if balance is not None:
                print(f"💰 Balance: ${balance:.2f}")
            else:
                print("❌ Account not found.")

        elif choice == "3":
            acc_number = input("Enter Account Number: ")
            try:
                amount = float(input("Enter amount to deposit: "))
                if bank.deposit(acc_number, amount):
                    print("✅ Deposit successful.")
                else:
                    print("❌ Deposit failed.")
            except ValueError:
                print("❌ Invalid amount.")

        elif choice == "4":
            acc_number = input("Enter Account Number: ")
            try:
                amount = float(input("Enter amount to withdraw: "))
                if bank.withdraw(acc_number, amount):
                    print("✅ Withdrawal successful.")
                else:
                    print("❌ Insufficient funds or invalid amount.")
            except ValueError:
                print("❌ Invalid amount.")

        elif choice == "5":
            from_acc = input("From Account: ")
            to_acc = input("To Account: ")
            try:
                amount = float(input("Amount to transfer: "))
                if bank.transfer(from_acc, to_acc, amount):
                    print("✅ Transfer successful.")
                else:
                    print("❌ Transfer failed. Check account numbers or balance.")
            except ValueError:
                print("❌ Invalid amount.")

        elif choice == "6":
            acc_number = input("Enter Account Number: ")
            details = bank.display_account_details(acc_number)
            print("\n" + details)

        elif choice == "7":
            print("👋 Exiting. Thank you for using our bank!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


=== Simple Banking System ===
1. Add Account
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Transfer Money
6. Display Account Details
7. Exit
Enter your choice: 1
Account Number: 101
Holder Name: Alice
Initial Balance: 500
 Account added successfully!


