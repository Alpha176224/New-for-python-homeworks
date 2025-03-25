import csv
import json

# Task 1: Library Management System
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException("Member cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException("This book is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, title, author):
        self.books[title] = Book(title, author)

    def add_member(self, name):
        self.members[name] = Member(name)

    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException("Book not found in the library.")
        self.members[member_name].borrow_book(self.books[book_title])

    def return_book(self, member_name, book_title):
        self.members[member_name].return_book(self.books[book_title])

library = Library()
library.add_book("Python Basics", "John Doe")
library.add_member("Alice")
library.borrow_book("Alice", "Python Basics")
library.return_book("Alice", "Python Basics")

# Task 2: Student Grades Management
with open("grades.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    grades = {}
    count = {}
    for row in reader:
        subject = row[1]
        grade = int(row[2])
        if subject in grades:
            grades[subject] += grade
            count[subject] += 1
        else:
            grades[subject] = grade
            count[subject] = 1
    avg_grades = {subject: grades[subject] / count[subject] for subject in grades}

with open("average_grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg in avg_grades.items():
        writer.writerow([subject, avg])

# Task 3: JSON Handling
with open("tasks.json", "r") as file:
    tasks = json.load(file)

def display_tasks():
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def calculate_stats():
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task["priority"] for task in tasks) / total_tasks
    print(f"Total tasks: {total_tasks}, Completed: {completed_tasks}, Pending: {pending_tasks}, Average Priority: {avg_priority}")

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def convert_json_to_csv():
    with open("tasks.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])

display_tasks()
calculate_stats()
save_tasks()
convert_json_to_csv()
