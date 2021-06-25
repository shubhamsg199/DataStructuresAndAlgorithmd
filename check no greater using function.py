def CheckNums(num1, num2):
    if num2 > num1:
         num1 = True
    elif num1 == num2:
         num1 = -1

    else:
        num1 = False

    return num1

print(CheckNums(4,4))