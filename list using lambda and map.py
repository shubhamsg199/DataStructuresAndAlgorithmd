list1 = []
q = int(input('enter how much nos you want to enter'))

for i in range(q):
    print("Enter number",i+1,end=" ")
    n=int(input())
    list1.append(n)

newlist = list(map(lambda x:x,list1))
newlist.sort()
print (newlist)

