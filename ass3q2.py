#function to check is fibonacci
def isfibo(n):
    if n in fibo:
        return True
    else:
        return False

#making a fiibonacci series upto 100 terms    
fibo=[0,1]
i=2
while(i<100):
    fibo.append(fibo[i-1]+fibo[i-2])
    i+=1
#taking input from user
t=int(input("No of testcases"))
while(t>0):
    n=int(input("enter a number"))
    if isfibo(n)==True:
        print(f"{n}   Isfibo")
    else:
        print(f"{n}   IsNotfibo")
    