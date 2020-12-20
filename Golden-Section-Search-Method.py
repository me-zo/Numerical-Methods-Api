
# The Below Code Calculates X  Using The Golden-Section Search Method 

import math as m

def D(Xl, Xu):
    return 0.618 * (Xu - Xl)


####################################### FOR Single Iterations #################################################        

def f(x):
    
    return 2 * x * m.cos(2 * x) - 3 * m.cos(5*x) + 2 * x  
    
    #  m.sin(0.2)
    #  m.cos(0.2)
    #  m.tan(0.2)
    #  m.pow(1, 2)   Square
    #  m.pow(1, 0.5)  Redical
    
    

xl = 0.5
xu = 1.5
Value = "max"

x1  =  xl + D(xl, xu)
x2  =  xu - D(xl, xu)
f(x1)
f(x2)

if Value == "max" :
    if (f(x2) > f(x1)):
        Xopt = x2
    else :
        Xopt = x1

if Value == "min" :
    if (f(x1) < f(x2)):
        Xopt = x1
    else :
        Xopt = x2

Err =abs( 0.382 * ((xu - xl)/Xopt) * 100 )

if (f(x1) > f(x2)):
    xl = X2       
else:
    xu = x1

print("\nNew Xl = " , xl)
print("\nNew Xu = " , xu)
print("\nD = " , D(xl, xu))
print("\nX1 = " , x1)
print("\nX2 = " , x2)
print("\nF(X1) = " , f(x1))
print("\nF(X2) = " , f(x2))
print("\nError = " ,Err , "%")


###############################################################################################################

####################################### FOR for N Iterations #################################################   

N = 5
Xlower = 0.5
Xupper = 1.5
Val = "max"

def F(x):
    result = 2 * x * m.cos(2 * x) - 3 * m.cos(5*x) + 2 * x  #Example Equation
    
    #  m.sin(0.2)
    #  m.cos(0.2)
    #  m.tan(0.2)
    #  m.pow(1, 2)   Square
    #  m.pow(1, 0.5)  Redical
    
    return result




print("\n Iteration |   Xl    |   Xu     |    D     |   X1     |   X2     |  F(x1)    |  F(X2)   |   E "
      "\n-----------------------------------------------------------------------------------------")
count = 0
for i in range (0, N):
    count +=1
    Xoptimal = 0
    X1 =  Xlower + D(Xlower, Xupper)
    X2 =  Xupper - D(Xlower, Xupper)
    F(X1)
    F(X2)
    
    if Val == "max" :
        if (F(X2) > F(X1)):
            Xoptimal = X2
        else :
            Xoptimal = X1
    
    if Val == "min" :
        if (F(X1) < F(X2)):
            Xoptimal = X1
        else :
            Xoptimal = X2

    E =abs( 0.382 * ((Xupper - Xlower)/Xoptimal) * 100 )
    
    print("     {0:1d}     | {1:.5f} | {2:.5f}  | {3:.5f}  | {4:.5f}  | {5:.5f}  "
          "| {6:.5f}   | {7:.5f}  | {8:.2f} % \n".format(count, Xlower, Xupper, D(Xlower,Xupper), X1, X2, F(X1), F(X2), E))   

    if (F(X1) > F(X2)):
        Xlower = X2
        
    else:
        Xupper = X1

