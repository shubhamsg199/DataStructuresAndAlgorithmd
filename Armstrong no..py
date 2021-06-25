


n = int(input('enter no. to check armstrong'))
sum = 0
temp = n

while n!=0:
    dig=temp%10
    sum +=dig**3
    temp = n//10
if sum == n:
    print (sum)
    print('Number is Armstrong')
else:
    print('Not Armstrong')







