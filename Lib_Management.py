import os
import pickle

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False
        self.issued_to = None
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

def create_book(book_list):
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")
    book = Book(book_id, title, author)
    book_list.append(book)
    save_books(book_list)
def display_all_books(book_list):
    for book in book_list:
        status = 'Issued' if book.is_issued else 'Available'
        issued_to = f", Issued to: {book.issued_to}" if book.is_issued else ''
        print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {status}{issued_to}")

def display_specific_book(book_list):
    book_id = input("Enter Book ID to search: ")
    for book in book_list:
        if book.book_id == book_id:
            status = 'Issued' if book.is_issued else 'Available'
            issued_to = f", Issued to: {book.issued_to}" if book.is_issued else ''
            print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {status}{issued_to}")
            return
    print('Book not found.')

def modify_book(book_list):
    book_id = input("Enter Book ID to modify: ")
    for  book in book_list:
        if book.book_id == book_id:
            book.title = input("Enter new Title: ")
            book.author = input("Enter new Author: ")
            save_books(book_list)
            print("Book record updated.")
            return
    print("Book not found.")

def delete_book_record(book_list):
    book_id = input("Enter Book ID to delete: ")
    for book in book_list:
        if book.book_id == book_id:
            book_list.remove(book)
            save_books(book_list)
            print("Book record deleted.")
            return
    print("Book not found.")

def create_student(student_list):
    student_id = input("Enter Student ID: ")
    name = input("Enter the Name: ")
    student = Student(student_id, name)
    student_list.append(student)
    save_students(student_list)

def display_all_students(student_list):
    for student in student_list:
        print(f"ID: {student.student_id}, Name: {student.name}")

def display_specific_student(student_list):
    student_id = input("Enter Student ID to search: ")
    for student in student_list:
        if student.student_id == student_id:
            print(f"ID: {student.student_id}, Name: {student.name}")
            return
    print("Student not found.")
def modify_student(student_list):
    student_id = input("Enter Student ID to modify: ")
    for student in student_list:
        if student.student_id == student_id:
            student.name = input("Enter new Name: ")
            save_students(student_list)
            print("Student record updated.")
            return
    print("Student not found.")
def delete_student_record(student_list):
    student_id = input("Enter Student ID to delete: ")
    for student in student_list:
        if student.student_id == student_id:
            student_list.remove(student)
            save_students(student_list)
            print("Student record deleted.")
            return
    print("Student not found.")

def save_books(book_list):
    with open('book.dat', 'wb') as f:
        pickle.dump(book_list, f)

def load_books():
    if os.path.exists('book.dat'):
        with open('book.dat', 'rb') as f:
            return pickle.load(f)
    return []

def save_students(student_list):
    with open('student.dat', 'wb') as f:
        pickle.dump(student_list, f)

def load_students():
    if os.path.exists('student.dat'):
        with open('student.dat', 'rb') as f:
            return pickle.load(f)
    return []

def issue_book(book_list, student_list):
    book_id = input("Enter Book ID to issue: ")
    student_id = input("Enter Student ID: ")
    for book in book_list:
        if book.book_id == book_id:
            if book.is_issued:
                print("Book is already issued.")
                return
            for student in student_list:
                if student.student_id == student_id:
                    book.is_issued = True
                    book.issued_to = student_id
                    save_books(book_list)
                    print(f"Book {book_id} issued to Student {student_id}")
                    return
            print("student not found.")
    print('Book not found.')

def deposit_book(book_list):
    book_id = input("Enter Book ID to deposit: ")

    for book in book_list:
        if book.book_id == book_id:
            if not book.is_issued:
                print("Book is not issued.")
                return
            book.is_issued = False
            book.is_issued = None
            save_books(book_list)
            print(f"Book {book_id} has been deposited.")
            return
    print("Book not found.")

def admin_menu(book_list, student_list):
    while True:
        print("\nADMINISTRATION MENU")
        print("1. CREATE STUDENT RECORD")
        print("2. DISPLAY ALL STUDENT RECORD")
        print("3. DISPLAY SPECIFIC STUDENT RECORD")
        print("4. MODIFY STUDENT RECORD")
        print("5. DELETE STUDENT RECORD")
        print("6. CREATE BOOK")
        print("7. DISPLAY ALL BOOKS")
        print("8. DISPLAY SPECIFIC BOOK")
        print("9. MODIFY BOOK")
        print("10. DELETE BOOK RECORD")
        print("11. EXIT TO MAIN MENU")
        choice = input("Enter your choice: ")
        if choice == '1':
            create_student(student_list)
        elif choice == '2':
            display_all_students(student_list)
        elif choice == '3':
            display_specific_student(student_list)
        elif choice == '4':
            modify_student(student_list)
        elif choice == '5':
            delete_student_record(student_list)
        elif choice == '6':
            create_book(book_list)
        elif choice == '7':
            display_all_books(book_list)
        elif choice == '8':
            display_specific_book(book_list)
        elif choice == '9':
            modify_book(book_list)
        elif choice == '10':
            delete_book_record(book_list)
        elif choice == '11':
            break
        else:
            print("Invalid choice. Please try again")

def main_menu():
    book_list = load_books()
    student_list = load_students()

    while True:
        print("\nMENU")
        print("1. BOOK ISSUE")
        print("2. BOOK DEPOSIT")
        print("3. ADMINISTRATION MENU")
        print("4. EXIT")
        choice = input("Enter your choice:")

        if choice == '1':
            issue_book(book_list, student_list)
        elif choice == '2':
            deposit_book(book_list)
        elif choice == '3':
            admin_menu(book_list, student_list)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main_menu()

