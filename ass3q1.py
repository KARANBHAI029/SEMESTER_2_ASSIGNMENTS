def digital_root(n):
    while(n//10!=0):
        sum1=0
        while(n>0):
            digit=n%10
            sum1=digit+sum1
            n=n//10
        n=sum1
    return n;  
def main():
    n=int(input("enter a number"))
    print(digital_root(n))
if __name__=='__main__':
    main()
n=int(input("enter a number"))
r=digital_root(n)
print(r)