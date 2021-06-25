list1=[]
for i in range(3):
    print("Enter name",i,end=" ")
    n=input()
    list1.append(n)
    for i in list1:
        if len(i) > 5:
            print(list1)
        else:
            print(error')
print(list1)
