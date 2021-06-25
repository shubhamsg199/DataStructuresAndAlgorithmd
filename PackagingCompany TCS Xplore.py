class Container:
    def __init__(self,id,length,breadth,height,status):
        self.id = id
        self.length = length
        self.breadth = breadth
        self.height = height
        self.status = status

    def getVolume(self):
        return self.length * self.breadth * self.height

class PackagingCompany:
    def __init__(self,clist):
        self.clist = clist

    def findContainersToPack(self,vol):
        for i in self.clist:
            r = i.getVolume()
            if i.status.lower() == "available" and r >= vol:
                i.status = "Used"

if __name__ == '__main__':
    clist = []
    n = int(input())
    for i in range(n):
        id = int(input())
        length = int(input())
        breadth = int(input())
        height = int(input())
        status = "Available"
        clist.append(Container(id,length,breadth,height,status))

    p = PackagingCompany(clist)
    vol = int(input())
    #res1 = p.findContainersToPack(vol)
    print("The Container Details:")
    p.findContainersToPack(vol)
    for i in clist:
        print(i.id,i.length*i.breadth*i.height,i.status)