# Easy:
# Store names
import operator


students = {}
pos = 1
while True:
    print("1. Add student")
    print("2. Stop")
    n = int(input("Enter choice: "))
    if n == 1:
        name = input("Enter name: ")
        students[pos] = name
        pos += 1
    elif n == 2:
        break

for key, value in students.items():
    print(f"{key}. Name: {value}")

# Search item
src = input("Enter name of student you want to search: ")
if src in students.values():
    print("Found")
else:
    print("Not found.")

# Remove duplicates
li = [1, 2,3,4,5,6,1,2,8,4,6,9,10,11,5,12,14,20,28,19,15,18]
print("Before removing duplicate: ", li)
print("Lenght : ", len(li))

li = list(set(li))
print("After removing duplicate: ", li)
print("Lenght : ", len(li))

# Medium:
# 4. Highest GPA
student = {
    "Alice": 3.8,
    "Bob": 3.5,
    "Charlie": 3.9,
    "David": 3.7
}
nm = ''
highestGPA = 0.0

for key, value in student.items():
    if student[key] > highestGPA:
        highestGPA = student[key]
        nm = key
print(f"{nm} got the highest GPA. Highest GPA: {highestGPA}")

# 5. Student ranking
stu = {
    "Alice": 3.8,
    "Bob": 3.5,
    "Charlie": 3.9,
    "David": 3.7
}

print(sorted(stu.items(), key=lambda rnk: rnk[1], reverse=True)) # rnk[1] sort based on index 1 (gpa)
# OR 
print(sorted(stu.items(), key=operator.itemgetter(1), reverse=True))
