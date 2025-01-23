# Initialize an empty list to store student names
student = []

# Loop to input names of 10 students
for i in range(10):
    # Prompt the user to enter the name of a student
    name = input("Enter the name of student")
    # Append the entered name to the student list
    student.append(name)

# Loop to iterate through the list of student names
for i in student:
    # Print the name reversed and truncated to a maximum of 15 characters
    print(i[:15][::-1])
