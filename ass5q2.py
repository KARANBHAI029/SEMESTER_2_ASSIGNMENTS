tets=int(input("enter number of test cases"))
k=(input("enter number of cuts  "))
list1=list(k.split())
for i in list1:
    max=0
    t=int(i)
    for j in range(int(i)):
        cuts=(t)*j
        t=t-1
        if cuts>max:
            max=cuts
    print(max)