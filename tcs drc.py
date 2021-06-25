n = int(input())
l = []
for i in range(n):
    k = int(input())
    l.append(k)

l2 = list(set(l))
l2.sort()
if n > 2:
    ele = l2[0]
    c = 0
    for j in (l2):
        if ele == j:
            c += 1
    if c == len(l2):
        print("Equal")
    else:
        print(l2[0], l2[1])
else:
    print("Invalid Input")
