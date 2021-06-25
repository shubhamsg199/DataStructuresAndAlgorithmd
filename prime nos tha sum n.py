def primenos(low,high):
    for i in range(low,high):
        for j in range(low+1,high):
            if i + j == 10:
                print("(%d,%d)"%(i,j),end=" ")






x,y = input().split()
op = primenos(int(x),int(y))