n = int(input())
l = []
for i in range(n):
    n2 = int(input())
    l.append(n2)
l.sort(reverse=True)
l2 = []
for i in l:
    if i not in l2:
        l2.append(i)
print(l2[1])