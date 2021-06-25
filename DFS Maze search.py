def isSafe(arr, x, y, n):
    if x < n and y < n and (arr[x][y] == 1 or arr[x][y] == 9):
        return True
    return False


def mazeSearch(arr, x, y, n, res, l, l2, c):
    if x == l[0][0] and y == l[0][1]:
        res[x][y] = 1
        l2.append([x, y])
        c[0] += 1
        return True
    # if x == n-1 and y == n-1:    ###This part of code is if we want to reach end of the matrix
    # return True
    if isSafe(arr, x, y, n):
        res[x][y] = 1
        l2.append([x, y])
        c[0] += 1

        if mazeSearch(arr, x + 1, y, n, res, l, l2, c):
            return True
        if mazeSearch(arr, x, y + 1, n, res, l, l2, c):
            return True
        # if mazeSearch(arr,x-1,y,n,res,l,l2,c):
        #     return True
        # if mazeSearch(arr,x,y-1,n,res,l,l2,c):
        #     return True
        res[x][y] = 0
        l2.remove([x, y])
        c[0] -= 1
        return False
    return False


if __name__ == "__main__":
    n = 3
    arr = [
        [1, 1, 1],
        [1, 1, 0],
        [0, 9, 0]
    ]
    res = [[0 for j in range(3)] for i in range(3)]
    l = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 9:
                l.append([i, j])
    l2 = []
    c = [0]
    if mazeSearch(arr, 0, 0, n, res, l, l2, c):
        for i in range(len(res)):
            for j in range(len(res)):
                print(res[i][j], end=" ")
            print()
        # for i in (l2):
        # print(i)
        print(l2)
        for i in c:
            print(i - 1)
