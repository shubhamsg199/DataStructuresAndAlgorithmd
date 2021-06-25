def routePairs(travelDist, forwardRouteList, returnRouteList):
    l = []
    d = {}
    k = 0
    for i in range(len(forwardRouteList)):
        for j in range(len(returnRouteList)):
            if forwardRouteList[i][1] + returnRouteList[j][1] == travelDist:
                l.append([forwardRouteList[i][0], returnRouteList[j][0]])
            elif forwardRouteList[i][1] + returnRouteList[j][1] < travelDist and forwardRouteList[i][1] + \
                    returnRouteList[j][1] > k:
                k = forwardRouteList[i][1] + returnRouteList[j][1]
                d[k] = [forwardRouteList[i][0], returnRouteList[j][0]]
    if l:
        return l
    else:
        if d:
            return d[max(d)]
        else:
            return []


dist = 10000
flist = [[1, 3000], [2, 5000], [3, 7000], [4, 1000]]
rlist = [[1, 7000], [2, 2000], [3, 5000], [4, 9000]]
# dist = 7000
# flist = [[1,2000],[2,4000],[3,6000]]
# rlist = [[1,1000]]

print(routePairs(dist, flist, rlist))
