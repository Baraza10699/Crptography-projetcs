def gcdList(ls):
    # Your code here; compute the gcd g of the list ls
    def gcd(a,b):
        while b!= 0:
            a,b = b,a%b
            
        return a
    x = 1
    g = ls[0]
    
    while x!=len(ls):
        g = gcd(g,ls[x])
        if g ==1:
            return 1
        else:
            x = x + 1
        
    return g




# def find_gcd(l):
#     def gcd(a, b):
#         while b:
#             a, b = b, a%b
#         return a
#     n =1
#     f = l[0]
#     while n != len(l):
#         f = gcd(f,l[n])
#         if  f == 1:
#             return 1
#         else:
#             n = n + 1          
#     return f