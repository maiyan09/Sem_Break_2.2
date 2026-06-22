# CLI Student Management System
students = {}
class Students:
    def __init__(self, id, name, dept, section):
        self.id = id
        self.name = name
        self.dept = dept
        self.section = section
    def showDetails(self):
        print(f"ID - {self.id}\nName - {self.name}\nDepartment - {self.dept}\nSection - {self.section}")
        
    def saveDetails(self):
        with open('student.txt', 'a') as file:
            file.write(f"ID - {self.id}\nName - {self.name}\nDepartment - {self.dept}\nSection - {self.section}\n")
# Features:
# 1 Add
def addStudent():
    id = input("Enter student ID: ").strip()
    if not id:
        print("Student ID cannot be empty.")
        return
    
    if id in students:
        print(f"Student with id {id} alreday exist.")
        return

    name = input("Enter student name: ")
    dept = input("Enter student Department: ")
    section = input("Enter student Section: ")
    
    students[id] = Students(id, name, dept, section)
    
# 2 Remove
def removeStudent():
    id = input("Enter student ID: ").strip()
    if not id:
        print("Student ID cannot be empty.")
        return
    if id in students:
        del students[id]
    else:
        print(f"Student with id {id} does not exist.")
        
# 3 Search
def searchStudent():
    id = input("Enter student ID: ").strip()
    if not id:
        print("Student ID cannot be empty.")
        return
    if id in students:
        students[id].showDetails()
    else:
        print(f"Student with id {id} does not exist.")
# 4 Save
def saveStudents():
    with open('student.txt', 'w') as file:
        for student in students.values():
            file.write(
                f"ID - {student.id}\n"
                f"Name - {student.name}\n"
                f"Department - {student.dept}\n"
                f"Section - {student.section}\n\n"
            )

    print("All student data saved successfully.")
# 5 Statistics

while True:
    try:
        print("\nCLI Student Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Save to File Student Information")
        print("5. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            addStudent()
        elif choice == 2:
            removeStudent()
        elif choice == 3:
            searchStudent()
        elif choice == 4:
            saveStudents()
        elif choice == 5:
            print("Successfully exit.")
            break
        else:
            print("Invalid choice!")
    except ValueError:
        print("Enter number not string..")
        
