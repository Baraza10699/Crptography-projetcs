def relatedkeys(g,p,A,c11,c12,m1,c21,c22):
    # your code here
    for i in range (1,101):
        for j in range(1,101):
            if modpow(c21,1,p) == (modpow(g,j,p) * modpow(c11,i,p))%p:
                ans1 = modpow(c12,-i,p)
                ans2 = modpow(m1,i,p)
                ans3 = modpow(A,-j,p)
                
                return modpow(ans1 * ans2 *ans3 * c22,1,p)

def modpow(a, n, m):
    if n<0:
        u = bezout (a,m)[1]
        return modpow(u,-n,m)
    if n == 1:
        return a % m
    x = modpow(a, n >> 1, m)
    x = (x * x) % m
    if (n & 1 == 1) == 1:  # if odd number
        x = (x * a) % m
    return x

def bezout(a,b):
    if b ==0:
        g,u,v = a,1,0
        return (g,u,v)
    else:
        u2,v2,u1,v1 = 1,0,0,1
        while b>0:
            q =a//b
            x,u,v = (a - b *q),(u2 -q*u1),(v2 - q * v1)
            a,b,u2,v2,u1,v1 = b,x,u1,v1,u,v
    g,u,v = a,u2,v2
    return g,u,v