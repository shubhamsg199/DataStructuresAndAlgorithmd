num = int(input())
temp = num
rev=0
sum = 0                                                                #### ASKED IN INFOSYS CODING ROUND ####
if len(str(num))==1:
    print(2*num)
else:
    while(temp==num):
        while(num>0):
            dig=num%10
            rev=rev*10+dig
            num=num//10
    while(temp!=rev):
        if temp == rev:
            print(rev)
        else:
            sum = temp + rev
            num = sum
            rev = 0
            temp = num
            while (num > 0):
                dig = num % 10
                rev = rev * 10 + dig
                num = num // 10

    print(rev)
