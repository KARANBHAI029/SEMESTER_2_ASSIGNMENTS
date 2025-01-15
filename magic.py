test=int(input("Enter the number of cases "))
while test>0:
    tot_box=int(input("Enter the Number of Box "))
    box=int(input("put coin in box number "))
    swaps=int(input("enter the number of swaps"))
    array = [i + 1 for i in range(tot_box)]  # Creates [1, 2, 3, ..., tot_box]
    # Perform swaps
    while swaps!=0:
        j=int(input("enter box A to swap with  "))
        k=int(input("enter box B  "))
        temp=array[j-1]
        array[j-1]=array[k-1]
        array[k-1]=temp
        swaps-=1
    # Find the box containing the coin
    for i in range(len(array)):
        if array[i] == box:
            print(f"Coin found at box {i+1}")
            break    
    test-=1        

