
n = int(input('enter no. to check armstrong\n'))
sum = 0
temp = n

while temp!=0:
    dig=temp%10
    sum +=dig**3
    temp = temp//10

if n==sum:
    print(n,'Number is Armstrong')
else:
    print('Not Armstrong')







