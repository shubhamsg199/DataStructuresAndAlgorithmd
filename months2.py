n=int(input("Enter the month no. :\n"))
list1=[1,3,5,7,8,10,12]
list2=[4,6,9,11]
if n==2:
    print("This Months has 28 Days")
if n in range(0,13):
    if n in list1:
      print("This Month has 31 Days")
    elif n in list2:
      print("This Months has 30 Days")
else:
    print("Invalid month number")