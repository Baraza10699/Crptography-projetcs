def gcd(a,b):
    bestyet = 1
    for d in range(1,a+1):
        if a%d == 0 and b%d == 0:
            bestyet = d
    return bestyet
