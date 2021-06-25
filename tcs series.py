# Q.4) Consider the following series: 1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187…
# This series is a mixture of 2 series – all the odd terms in this series form a geometric series
# and all the even terms form yet another geometric series. Write a program to find the
# Nth termin the odd series.
# The value N in a positive integer that should be read from STDIN. The Nth term that is
# calculated by the program should be written to STDOUT. Other than value of n thterm,no
# other character / string or message should be written to STDOUT. For example , if N=16,
# the 16th term in the series is 2187, so only value 2187 should be printed to STDOUT.

def evenval(n):
    val = 1
    a = int(n/2)
    for i in range(2,a+2,1):    ## TCS Coding Question ##
        val = val*2
    return val
def oddval(n):
    val = 1
    b = int(n/2)
    for i in range(3,b+2,1):
        val = val*3
    return val
n = int(input())
if n==1 or n==2:
    print("1")
elif n%2==0:
    print(oddval(n))
elif n%2!=0:
    print(evenval(n))
