n = int(input("How many numbers do you want to check? "))  # Number of inputs

for _ in range(n):  # Loop for each number
    num = input("\nEnter the number: ")
    numlist = list(num)
    count = 0

    for j in numlist:
        i = int(j)
        if i != 0 and int(num) % i == 0:  # Avoid division by zero
            count += 1

    print(f"Number: {num}, Count of divisible digits: {count}")
