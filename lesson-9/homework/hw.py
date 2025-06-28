import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
c = Circle(5)
print("Radius:", c.radius)
print("Area:", c.area())
print("Perimeter:", c.perimeter())

from datetime import datetime
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
    def get_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age
person1 = Person("Ali", "Uzbekistan", "1995-06-15")

class Calculator:
    def __init__(self):
        pass  
    def add(self, a, b):
        return a + b  
    def subtract(self, a, b):
        return a - b  
    def multiply(self, a, b):
        return a * b  
    def divide(self, a, b):
        if b == 0:
            return "0 ga bo‘lish mumkin emas!"
        return a / b 
calc = Calculator()

import math
class Shape:
    def area(self):
        raise NotImplementedError("area() metodi hali aniqlanmagan")
    def perimeter(self):
        raise NotImplementedError("perimeter() metodi hali aniqlanmagan")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        # Geron formulasi
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 4, 5)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, value):
               if self.root is None:
            self.root = Node(value)
        else:
            curr = self.root
            while True:
                if value < curr.value:
                    if curr.left is None:
                        curr.left = Node(value)
                        break
                    curr = curr.left
                elif value > curr.value:
                    if curr.right is None:
                        curr.right = Node(value)
                        break
                    curr = curr.right
                else:
                    break  
    def search(self, value):
        curr = self.root
        while curr:
            if value == curr.value:
                return True
            elif value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return False

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)  
    def pop(self):
        if not self.is_empty():
            return self.items.pop()  
        else:
            return "Stack bo‘sh!"
    def is_empty(self):
        return len(self.items) == 0  
    def peek(self):
        if not self.is_empty():
            return self.items[-1] 
        else:
            return "Stack bo‘sh!"
    def size(self):
        return len(self.items) 

class Node:
    def __init__(self, data):
        self.data = data   
        self.next = None  
class LinkdList:
    def __init__(self):
        self.head = None  
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:      
            self.head = new_node
        else:
            current = self.head
            while current.next:  
                current = current.next
            current.next = new_node
    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev is None:       
                    self.head = current.next
                else:
                    prev.next = current.next
                return True 
            prev = current
            current = current.next
        return False 
    def display(self):
        current = self.head
        if not current:
            print("Ro'yxat bo‘sh.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

class ShoppingCart:
    def __init__(self):
        self.items = {} 
    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name][1] += quantity 
        else:
            self.items[name] = [price, quantity]
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            print(f"{name} savatchada topilmadi.")
    def get_total(self):
        total = 0
        for price, quantity in self.items.values():
            total += price * quantity
        return total
    def show_cart(self):
        if not self.items:
            print("Savatcha bo‘sh.")
            return
        print("🛒 Savatchadagi mahsulotlar:")
        for name, (price, quantity) in self.items.items():
            print(f"- {name}: {quantity} dona x {price} = {price * quantity}")
        print(f"Umumiy narx: {self.get_total()} so'm")

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
        print(f"{item} stack’ga qo‘shildi.")
    def pop(self):
        if not self.is_empty():
            removed = self.items.pop()
            print(f"{removed} stack’dan olib tashlandi.")
            return removed
        else:
            print("Stack bo‘sh! Pop mumkin emas.")
            return None
    def is_empty(self):
        return len(self.items) == 0
    def display(self):
        if self.is_empty():
            print("Stack bo‘sh.")
        else:
            print("Stack elementlari (eng ustidan boshlab):")
            for item in reversed(self.items):
                print(item)

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
        print(f"{item} navbatga qo‘shildi.")
    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"{removed} navbatdan olib tashlandi.")
            return removed
        else:
            print("Navbat bo‘sh! Hech narsa olib bo‘lmaydi.")
            return None
    def is_empty(self):
        return len(self.items) == 0
    def display(self):
        if self.is_empty():
            print("Navbat bo‘sh.")
        else:
            print("Navbatdagi elementlar:")
            for item in self.items:
                print(item)

class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} so'm depozit qilindi.")
        else:
            print("Notog‘ri summa!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so'm yechildi.")
        else:
            print("Yetarli mablag‘ mavjud emas yoki noto‘g‘ri summa!")

    def check_balance(self):
        print(f"{self.name} hisobidagi balans: {self.balance} so'm")
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = {} 
    def create_account(self, name, account_number, initial_balance=0):
        if account_number in self.accounts:
            print("Bunday hisob raqam allaqachon mavjud.")
        else:
            self.accounts[account_number] = BankAccount(name, account_number, initial_balance)
            print(f"Hisob raqam yaratildi: {name}, raqam: {account_number}")
    def get_account(self, account_number):
        return self.accounts.get(account_number, None)
    def display_all_accounts(self):
        print("\n🏦 Bankdagi barcha hisob raqamlari:")
        for acc in self.accounts.values():
            print(f"{acc.name} ({acc.account_number}): {acc.balance} so'm")


bank = Bank()


bank.create_account("Ali", "ACC123", 100000)
bank.create_account("Vali", "ACC456", 50000)


account = bank.get_account("ACC123")
if account:
    account.deposit(25000)
    account.withdraw(50000)
    account.check_balance()

bank.display_all_accounts()












