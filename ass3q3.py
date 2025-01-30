def UtopianTree(height,n):
    #checking if no cylce is given
    if n==0:
        return height
    #for monsoon
    else:
        height=height*2
        n=n-1
    #for summer
    if n!=0:
        height=height+1
        n=n-1
    #check if n!=0 so we recall the function to find height
    if n!=0:
        return UtopianTree(height,n)
    #if n==0 the return the height
    else:
        return height
t=int(input("No of testcases"))
while(t>0):
    height=1
    n=int(input("Enter Number of cycle"))
    growth=UtopianTree(height,n)
    print(f"Growth of tree is : {growth} ")
    t=t-1