class Player:
    def __init__(self, name, country, age, matches, runs, wickets):
        self.name = name
        self.country = country
        self.age = age
        self.matches = matches
        self.runs = runs
        self.wickets = wickets


class Team:
    def getMinRuns(self, plist):
        c = plist[0].runs
        for i in plist:
            if i.runs < c:
                c = i.runs
                n = i.name
                q = i.country

        print(n, c, q, sep="\n")

    def getMaxWickets(self, plist):
        c = 0
        for i in plist:

            if i.wickets > c:
                c = i.wickets
                n = i.name
                q = i.country

        print(n, c, q, sep="\n")


if __name__ == '__main__':
    plist = []
    n = int(input())
    for i in range(n):
        name = input()
        country = input()
        age = int(input())
        matches = int(input())
        runs = int(input())
        wickets = int(input())
        plist.append(Player(name, country, age, matches, runs, wickets))

    team = Team()
    team.getMinRuns(plist)
    team.getMaxWickets(plist)
