import math
def ppFactor(N):
    # Your code here: make a list "factors"
    x = 2
    
    factors =[]
    
    for i in range (2,pow(2,16)):
        counter = 0
        while N %i == 0:
            counter +=1
            N = N //i
        if counter !=0:
            factors.append(pow(i,counter))
         
    return factors
