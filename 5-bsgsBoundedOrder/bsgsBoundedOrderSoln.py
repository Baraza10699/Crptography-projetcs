import math
def bsgsBoundedOrder(g,h,p,q):
    # Your code here
    n = math.floor(math.sqrt(q)) + 1
    v = pow(g, n * (p - 2), p)
    gtl = {}
    g1 = 1

    for i in range(n):
        gtl[g1] = i
        g1 = (g1 * g) % p

    h1 = h

    for j in range(n):
        if h1 in gtl:
            return j * n + gtl[h1]
        h1 = (h1 * v) % p
    return x





