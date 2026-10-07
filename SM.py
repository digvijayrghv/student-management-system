##School Management System
#================================================================================================
#Student portal
#================================================================================================
class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

#This will calculate percentage
    def percentage(self):
        return sum(self.marks)/len(self.marks) 

#This will choose a suitable grade according to the percentage
    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        elif percentage >= 40:
            return "E"
        elif percentage >= 30:
            return "Fail..."
        else:
            print("Error")

#This will print the detais of any student
    def display(self):
        print("\n-------Student Details-------") 
        print("ID-", self.student_id) 
        print("Name-", self.name)
        print("Marks-", self.marks)
        print("Percentage-", round(self.percentage(),2),"%" )
        print("Grade-", self.grade())

#================================================================================================
#NEW CLASS
# Office Manager this will do 
#✅ Student Add
#✅ Student Search
#✅ Student Display
#================================================================================================

class student_management:
    def __init__(self):
        self.students = [] 

    def Add_student(self):
        student_id = input("Enter student's ID- ")
        student_name = input("Enter student's name- ")

        marks = [] 
        
        for i in range(3):
            mark = float(input("Enter marks of subject- "))
            marks.append(mark)

        student = Student(student_id, student_name, marks)
        self.students.append(student)

        print("Student added sucessfully")
    
    def display_student(self):
        if not self.students:
            print("No Students Found!")
        else:
            for student in self.students:
                student.display()

    def search_student(self):
        sid = input("Enter student ID to search- ")

        for student in self.students:
            if student.student_id == sid:
                student.display()
                return
            
        print("Student not found!")

def main():
    sms = student_management()
    while True:
        print("\n-----student management system------")
        print("1) Add Student")
        print("2) Display all students")
        print("3) Search students")
        print("4) Exit")

        choice = input("Enter your choice- ")
        if choice == "1":
            sms.Add_student()
        elif choice == "2":
            sms.display_student()
        elif choice == "3":
            sms.search_student()
        elif choice == "4":
            print("Thankyou")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()