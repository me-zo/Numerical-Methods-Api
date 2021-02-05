import math as m

# Here we simply give the input needed as The Following:
# ( equation ) First Specify if the input is an equation ( 1 ) or only a single application of the rule ( 0 )
# ( Xlower ) & ( Xupper ) The Upper And Lower Limits
# (Val) Specifies if you want the maximum ( max ) or the minimum ( min ) Value
# If The Equation was set to "0" you need to provide The Values F(x1), F(x2), x1 and x2. if not selected keep 0
# If The Equation was set to "1" you need to provide The Equation in the function ( F ) if not selected keep 0
# ( n ) is the number of Iterations needed

equation = 0

Xlower =  5

Xupper =  7.3

Val = "max"

Fx1 =  1231

Fx2 = 32123

X1 =  24332

X2 = 12

def F(x): return  3*m.exp(-x) + 2.5*x**-2 + 8.7*x*m.cos(x) - 9.4

n = 5

print("\n\n______________{    INTERVAL     }__________________________________________________________________")
print("\n Iteration |   Xl    |   Xu     |    D     |   X1     |   X2     |  F(x1)    |  F(X2)   |   Error "
      "\n---------------------------------------------------------------------------------------------------")
def D(Xl, Xu): return 0.618 * (Xu - Xl) 
for i in range (n):
    if equation == 1 :
        Xoptimal = 0; X1 =  Xlower + D(Xlower, Xupper); X2 =  Xupper - D(Xlower, Xupper)
        if Val == "max" :
            if (F(X2) > F(X1)): Xoptimal = X2
            else : Xoptimal = X1
        if Val == "min" :
            if (F(X1) < F(X2)):  Xoptimal = X1
            else : Xoptimal = X2           
    elif equation == 0:
        Xoptimal = 0
        if Val == "max" :
            if (Fx2 > Fx1): Xoptimal = X2
            else : Xoptimal = X1
        if Val == "min" :
            if (Fx1 < Fx2): Xoptimal = X1
            else :  Xoptimal = X2
    E =abs( 0.382 * ((Xupper - Xlower)/Xoptimal) * 100 )
    if equation == 1 :
        print("     {0:1d}     | {1:.5f} | {2:.5f}  | {3:.5f}  | {4:.5f}  | {5:.5f}  "
            "| {6:.5f}  | {7:.5f} | {8:.2f} % \n".format(i, Xlower, Xupper, D(Xlower,Xupper), X1, X2, F(X1), F(X2), E))  
    if equation == 0 :
        print("     {0:1d}     | {1:.5f} | {2:.5f}  | {3:.5f}  | {4:.5f}  | {5:.5f}  "
            "| {6:.5f}  | {7:.5f} | {8:.2f} % \n".format(i, Xlower, Xupper, D(Xlower,Xupper), X1, X2, Fx1, Fx2, E))   
    if (F(X1) > F(X2)): Xlower = X2
    else: Xupper = X1
# Finally displaying the solution while providing the percentage of error with each iteration  
