s = input()
l = list(s)
c = 1
for i in range(0,len(s)-1):
    if s[i] == s[i+1]:
        c +=1
    else:
        print((c,s[i]),end=" ")
        c = 1
print((c,s[i]),end=" ")
