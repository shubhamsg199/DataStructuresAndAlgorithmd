def canCompleteCircuit(A, B):
    total = 0
    tank = 0
    index = 0
    for i in range(len(A)):
        consume = A[i] - B[i]
        tank += consume
        if tank < 0:
            index = i + 1
            tank = 0
        total += consume
    if total < 0:
        return -1
    else:
        return index
a = (1,2,3,4,5)
b = (3,4,5,1,2)
print(canCompleteCircuit(a,b))