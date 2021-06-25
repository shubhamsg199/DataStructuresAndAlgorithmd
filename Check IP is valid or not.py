n = input()
n1 = (n.replace("."," "))
f = n1.split()
#print(f)
list1 = [int(i) for i in n1.split() if i.isdigit()]
a = 0
for i in list1:
    if i>255:
        a += 1
if a:
    print("Invalid")
else:
    print("Valid")
