def ways(m, n, memo={}):
    c = m, ",", n
    if c in memo:
        return memo[c]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[c] = ways(m - 1, n) + ways(m, n - 1)
    return memo[c]


print(ways(112, 18))
