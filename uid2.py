n = int(input("enter no"))#s
s=0                       #k
while (n>0):
    dig=n%10
    s=s+dig
    n=n//10
k=0
while s>0:
    z=s%10
    k=k+z
    s=s//10
    print(k)