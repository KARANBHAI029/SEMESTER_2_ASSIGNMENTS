# 

n = int(input("Enter the Number of Guests: "))
heights = []
swaps = 0

for k in range(n):
    height = int(input(f"Enter the height of guest {k+1}: "))
    heights.append(height)

for i in range(n):
    if i + 1 != heights[i]:
        swaps += 1
        for j in range(n):
            if i + 1 == heights[j]:
                heights[i], heights[j] = heights[j], heights[i]
                break

print(f"Total number of swaps are: {swaps}")
