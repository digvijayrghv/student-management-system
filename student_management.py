"""
Simple Student Management System
- Add, view, search, update, delete students
- Data is saved in students.json so it is not lost when you close the program
"""

import json
import os

FILE_NAME = "students.json"


# ---------- File handling ----------
def load_students():
    """Load students from the file. Return empty dict if file doesn't exist."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}


def save_students(students):
    """Save students to the file."""
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)


# ---------- Features ----------
def add_student(students):
    roll = input("Enter roll number: ").strip()
    if roll in students:
        print("A student with this roll number already exists!")
        return

    name = input("Enter name: ").strip()
    age = input("Enter age: ").strip()
    course = input("Enter course: ").strip()
    marks = input("Enter marks: ").strip()

    students[roll] = {"name": name, "age": age, "course": course, "marks": marks}
    save_students(students)
    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No students found.")
        return

    print("\n{:<8} {:<15} {:<5} {:<12} {:<6}".format("Roll", "Name", "Age", "Course", "Marks"))
    print("-" * 50)
    for roll, info in students.items():
        print("{:<8} {:<15} {:<5} {:<12} {:<6}".format(
            roll, info["name"], info["age"], info["course"], info["marks"]))


def search_student(students):
    roll = input("Enter roll number to search: ").strip()
    if roll in students:
        info = students[roll]
        print(f"\nRoll   : {roll}")
        print(f"Name   : {info['name']}")
        print(f"Age    : {info['age']}")
        print(f"Course : {info['course']}")
        print(f"Marks  : {info['marks']}")
    else:
        print("Student not found.")


def update_student(students):
    roll = input("Enter roll number to update: ").strip()
    if roll not in students:
        print("Student not found.")
        return

    print("Leave blank to keep the old value.")
    info = students[roll]
    for field in ["name", "age", "course", "marks"]:
        new_value = input(f"Enter new {field} ({info[field]}): ").strip()
        if new_value:
            info[field] = new_value

    save_students(students)
    print("Student updated successfully!")


def delete_student(students):
    roll = input("Enter roll number to delete: ").strip()
    if roll in students:
        del students[roll]
        save_students(students)
        print("Student deleted successfully!")
    else:
        print("Student not found.")


# ---------- Main menu ----------
def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
