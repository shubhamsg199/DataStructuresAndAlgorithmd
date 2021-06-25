def TimeConvert(num):
    a = num // 60
    b = num - (a * 60)
    return "hrs"':'.join([str(a), str(b),])
x = int(input('enter the no:\n'))
print(TimeConvert(x))