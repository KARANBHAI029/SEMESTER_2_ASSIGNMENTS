dict1={}
n = int(input("Enter the number of elements in the dictionary: "))
for _ in range(n):
    key = input("Enter product: ")
    value = input("Enter value: ")
    dict1[key]=value
print(dict1)

while True:
    key2=input("enter product to get value  ")
    if key2.lower()=="stop":
        print("exiting the service:")
        break
    elif key2 in dict1:
        print(f"The value for '{key2}' is: {dict1[key2]}")
    else:
        print("Product not found")