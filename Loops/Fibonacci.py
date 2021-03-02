first=0
second=1
#n = no. of terms to be printed 
n=int(input("Enter n: "))
while n:
    print(first,end=" ")
    t = first + second
    first=second
    second=t
    n -= 1