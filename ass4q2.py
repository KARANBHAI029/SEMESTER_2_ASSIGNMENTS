def countsquare(a, b):
    count = 0
    for i in range(a, b + 1):
        x = i ** 0.5  # Square root of i
        if x == int(x):  # Check if x is an integer (perfect square)
            count += 1
    return count

a = 3
b = 9
print(countsquare(a, b))  # Output: 2 (4 and 9)
