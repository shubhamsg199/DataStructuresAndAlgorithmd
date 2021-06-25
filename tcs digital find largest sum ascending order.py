l = [2,201,2,3,200,4,5]
l2 = []
sum = 0
temp = 0
for i in l:
    if temp < i:
        sum += i
    else:
        l2.append(sum)
        sum = i
    temp = i
l2.append(sum)
print(l2)