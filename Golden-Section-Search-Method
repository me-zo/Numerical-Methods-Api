
# The Below Code Calculates X  Using The Golden-Section Search Method 

import math as m
Xlower = 0.5
Xupper = 1.5
Val = "max"

def F(x):
    result = 2 * x * m.cos(2 * x) - 3 * m.cos(5*x) + 2 * x  #Example Equation
    return result

def D(Xlower, Xupper):
    return 0.618 * (Xupper - Xlower)

print("\n Iteration |   Xl    |   Xu    |    D    |   X1    |   X2    |  F(x1)   |  F(X2)  |   E "
      "\n-----------------------------------------------------------------------------------------")
count = 0
for i in range (0, 7):
    count +=1
    Xoptimal = 0
    X1 = Xlower + D(Xlower, Xupper)
    X2 = Xupper - D(Xlower, Xupper)
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
    
    print("     {0:1d}     |  {1:.4f} | {2:.4f}  | {3:.4f}  | {4:.4f}  | {5:.4f}  "
          "| {6:.4f}   | {7:.4f}  | {8:.2f}  ".format(count, Xlower, Xupper, D(Xlower,Xupper), X1, X2, F(X1), F(X2), E))   

    if (F(X1) > F(X2)):
        Xlower = X2
        
    else:
        Xupper = X1
        
 
