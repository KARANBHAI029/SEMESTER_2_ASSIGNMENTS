print("part a")
# Create the list
intlist=[]
for i in range(50):
    intlist.append(i)
    # Print the list
for i in range(50):
    print(intlist[i])   


print("part b")
# Create the list
sqrlist=[]
for i in range(0,51):
    sqrlist.append(i)
    # Print the list
for i in range(1,50):
    print(sqrlist[i]**2)   


print("part c")  
# Create the list
char_list = [chr(97 + i) * (i + 1) for i in range(26)]

# Print the list
print(char_list)


