l = [14,33,27,10,35,19,42,44]
length = len(l)
for i in range(len(l)):
    min = i
    for j in range(i+1,len(l)):
        if l[min] > l[j]:
            min = j
    l[i],l[min] = l[min],l[i]
print(l)
