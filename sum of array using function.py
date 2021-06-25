from array import *


def simpleArraySum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


n = int(input('enter the size of array'))

arr =[]
for i in range(n):
    print("enter number", end=" ")
    q = int(input())
    arr.append(q)

print(simpleArraySum(arr))
