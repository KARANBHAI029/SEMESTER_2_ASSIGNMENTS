num=int(input("Enter a number to find factorial "))
fact =1
i=1
while i<=num:
    fact*=i
    i+=1
print("factorial of",num ,fact)