def bezout(a, b):
    if b == 0:
        g, u, v = a, 1, 0
        return g, u, v
    else:
        u2, v2, u1, v1 = 1, 0, 0, 1
        while b > 0:
            q = a // b
            x, u, v = (a - b * q), (u2 - q * u1), (v2 - q * v1)
            a, b, u2, v2, u1, v1 = b, x, u1, v1, u, v
    g, u, v = a, u2, v2
    return g, u, v
