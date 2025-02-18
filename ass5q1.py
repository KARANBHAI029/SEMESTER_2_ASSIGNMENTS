num1=int(input("enter number 1  "))
num2=int(input("enter number 2  "))
max=0
for i in range(num1,num2):
    for j in range(num1,num2):
        if i^j>max:
            max=i^j
print(max)