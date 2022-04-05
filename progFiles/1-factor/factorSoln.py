def factor(n):
    #     Your code here. Find p and q with p,q > 1 and pq = n.
    #     The order of p and q does not matter (e.g. if n=35, either 3,5 or 5,3 will be accepted
    #
    factors = []
    for i in range(1, n + 1):
        
            if n % i == 0:
                factors.append(i)
                n /= i
            else:
                i += 1
    return factors[1], factors[2]

#     factors = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             factors.append(i)


     
