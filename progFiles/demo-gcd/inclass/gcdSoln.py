def gcdOld(a,b):
    # Naive trial division
    bestyet = 1
    for d in range(1,a+1):
        if a%d == 0 and b%d == 0:
            bestyet = d
    return bestyet

def gcd(a,b):
    # Euclidean algorithm
    while b != 0:
        a,b = b,a%b #Slick 1-liner!
    return a
