#ADDITION OF MARKS (DICTIONARY)

d = {'English':int(input("Enter your  marks")),'Maths':int(input("enter ur marks")),'Science':int(input("enter ur marks"))}
s=0
for i in d.values():
    s += i
print("The Total Score is" ,s)

