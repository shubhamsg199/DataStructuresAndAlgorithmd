def FirstFactorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i

    return fact


FirstFactorial(4)
# keep this function call here
print(FirstFactorial(4))
