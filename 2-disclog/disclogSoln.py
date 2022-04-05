
import math
def disclog(g,h,p):
    # Your code here
    N = int(math.ceil(math.sqrt(p-1)))
    t = {}
    
    for  i in range (N):
        t[pow(g,i,p)] = i
    c = pow(g,N*(p-2),p)
    
    for j in range(N):
        y = (h* pow(c,j,p))%p
        if y in t:
            return j *N + t[y]
    return None





