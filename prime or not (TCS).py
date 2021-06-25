#n = int(input())
l = []
for i in range(1,6):
    l.append(int(input()))
for i in l:                             ## TCS Coding Question ##
    for j in range(2,i):
        if i%j==0:
            print("{} is not prime".format(i))
            break
    else:
        print("{} is prime".format(i))