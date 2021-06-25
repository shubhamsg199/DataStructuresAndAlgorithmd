
#[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
def rotate(matrix):
    k = 0
    l = []
    l1 = []
    for i in range(len(matrix)):
        for i in range(len(matrix) - 1,-1,-1):
            l1.append(matrix[i][k])
        k +=1
        l.append(l1)
        l1 = []
    return l
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print((rotate(matrix)))
