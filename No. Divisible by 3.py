#LIST OF NO. DIVISIBLE BY 3

list2=[]
for i in range (1,11):
    print("enter number",i,end=" ")
    n=int(input())
    if n%3==0:
        list2.append(n)
print(list2)
