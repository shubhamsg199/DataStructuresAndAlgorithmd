name = input("Enter your full name\n")
name = name.replace(" ","")
if name.isalpha():
    n = input("Enter your Mobile No.\n")
    if n.isdigit()==True and len(n) == 10:
        pincode = str(input("Enter your Pincode \n"))
        if pincode.isdigit()==True and len(pincode) == 6:
            Account = input("Enter the account type you want: 0-personal,1-Private,2-Company,3=NGO,4-Govt,5-Defence\n")
            if Account.isdigit() == True and len(Account) == 1:
                a = name[0] + name[1]
                s = 0

                for i in n:
                    s += int(i)
                c = 0
                for j in str(s):
                    c += int(j)

                    f = 0
                for k in str(c):
                    f += int(k)

                if f == 1:
                    e = "!"
                elif f == 0:
                    e = ")"

                elif f == 2:
                    e = "@"
                elif f == 3:
                    e = "#"

                elif f == 4:
                    e = "$"

                elif f == 5:
                    e = "%"

                elif f == 6:
                    e = "^"

                elif f == 7:
                    e = "&"

                elif f == 8:
                    e = "*"

                elif f == 9:
                    e = "("




                print("Your unique id is " + pincode + a + e + Account)
            else:
                print("Enter Valid choice")
        else:
            print("Please Enter Valid Pincode")
    else:
        print("Enter Valid Mobile no.")
else:
    print("Error..!Please enter alphabets")