# n = int(input())
# s = str(n)
# if n < 10:
#     print(n + 10)
# else:
#     l= []
#     for i in range(n,n*n):
#         c = 1
#         v = str(i)
#         for j in range(len(s)):
#             c = c * int(v[j])
#         if c == n:
#             l.append(i)
#             break
# if l :
#     print(l[0])
# else:
#     print("Not Possible")
def findSmallest(n):
    if n < 10:
        print(n + 10)
        return
    res = []
    for i in range(9, 1, -1):
        while n % i == 0:
            n = n / i
            res.append(i)
    if n > 10:
        print("Not Possible")
        return
    c = 0
    for i in reversed(res):
        c = i + c *10
    print(c)

findSmallest(int(input()))

