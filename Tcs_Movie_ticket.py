class Movie:
    def __init__(self,mid,mname,tcost,tcategory="Default"):
        self.mid = mid
        self.mname = mname
        self.tcost = tcost
        self.tcategory = tcategory

    def Price_category(self):
        if self.tcost > 0 and self.tcost < 150:
            self.tcategory = "General"
        elif self.tcost >= 150 and self.tcost < 250:
            self.tcategory = "Silver"
        elif self.tcost >= 250 and self.tcost < 350:
            self.tcategory = "Gold"
        elif self.tcost >= 350:
            self.tcategory = "Platinum"

class Movie_ticket:
    def __init__(self,cname,mname,vcount,ttcost):
        self.cname = cname
        self.mname = mname
        self.vcount = vcount
        self.ttcost = ttcost

def getCategoryWiseCount(mlist):
    d = {}
    for i in mlist:
        i.Price_category()
    for i in mlist:
        if i.tcategory not in  d.keys():
            d[i.tcategory] = 1
        else:
            d[i.tcategory] = d[i.tcategory]+1
    return d

def bookMovieTicket(mlist,cname,mname,vcount):
    total_cost = 1
    for i in mlist:
        if i.mname.lower() == mname.lower():
            total_cost = i.tcost*vcount
            return total_cost

if __name__ == "__main__":
    l=[]
    n = int(input())
    for i in range(n):
        a = int(input())
        b = input()
        c = int(input())
        l.append(Movie(a,b,c))

    cname = input()
    mname = input()
    vcount = int(input())
    obj1 = getCategoryWiseCount(l)
    obj2 = bookMovieTicket(l,cname,mname,vcount)
    print("Category wise Ticket count")
    for x,y in obj1.items():
        print(x,":",y,sep="")
    print(cname,obj2)



