n = int(input())
l = list(map(int,input().split()))
a,b = input().split()
f1 = -1
f2 = -1
for i in range(n):      ## TCS Coding Question ##
    if l[i]==int(a):
        f1 = i
    if l[i]==int(b):
        f2 = i
if not f1:
    print("e1 index:", -1)
else:
    print("e1 index:",f1)
if not f2:
    print("e2 index:", -1)
else:
    print("e2 index:", f2)