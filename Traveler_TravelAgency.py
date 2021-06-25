class Traveler:
    def __init__(self,name,traveledcountry,age,country):
        self.name = name
        self.traveledcountry = traveledcountry
        self.age = age
        self.country = country


class TravelAgency:
    def __init__(self,tlist,):
        self.tlist = tlist

    def countTravelersTraveledCountry(self,countryname):
        c = 0
        for i in self.tlist:
            for j in  i.traveledcountry:
                if j == countryname:
                    c += 1
        return c

    def getTravelerTravelledMaxCountry(self):
        c = 0
        l1 = []
        for i in self.tlist:
            if len(i.traveledcountry) > c:
                c = len(i.traveledcountry)
                l1.append(i.name)
        return l1[0]

if __name__ == '__main__':
    l = []
    n = int(input())
    for i in range(n):
        name = input()
        k = int(input())
        traveledcountry = []
        for j in range(k):
            traveledcountry.append(input())
        age = int(input())
        country = input()
        l.append(Traveler(name,traveledcountry,age,country))
    t = TravelAgency(l)
    nameofcountry = input()
    print(t.countTravelersTraveledCountry(nameofcountry))
    print(t.getTravelerTravelledMaxCountry())
