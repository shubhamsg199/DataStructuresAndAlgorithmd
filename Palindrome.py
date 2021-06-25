n = int(input("Enter the number to check palindrome\n"))
dup = n
rev=0
while n!=0:
    dup=n%10
    rev=rev*10+dup
    n=n//10
print(rev)
