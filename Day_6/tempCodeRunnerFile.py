# Practice
# # Save notes
# while True:
#     try:
#         print("1. Save note")
#         print("2. Leave")
#         n = int(input("Enter choice: "))
#         if n == 1:
#             note = input("Write your note: ")
#             with open('note.txt', 'a') as file:
#                 file.write('- ' + note + '\n')
#         elif n == 2:
#             break
#     except ValueError as v:
#         print("Error occurs: Enter number 1 or 2")
    
# # Read file
# with open('note.txt', 'r') as read:
#     contents = read.read()
#     print(contents)