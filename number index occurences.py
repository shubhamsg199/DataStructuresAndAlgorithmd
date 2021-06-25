n = int(input())
list1 = list(map(int,input().split()))
n2 = int(input())
n3 = 0
for i in range(len(list1)):     ## TCS coding Question ##
    if list1[i]==n2:
        n3 = n3*10+i

    elif list1[i]!=n2:
        a = "NO OCCURENCES"
if (n3):
    print(n3)
else:
    print(a)
