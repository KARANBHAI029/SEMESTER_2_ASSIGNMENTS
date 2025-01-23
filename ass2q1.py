str1 = input("Enter the string: ")
new_str = ""

for i in range(len(str1)):
    if i % 2 != 0:  # Check if the index is odd
        new_str += str1[i].upper()
    else:
        new_str += str1[i]

print(new_str)
