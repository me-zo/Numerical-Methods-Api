import math as m
from scipy.misc import derivative

# Here we simply give the input needed as The Following:
# ( Equation ) First Specify if the input is an equation ( 1 ) or only a single application of the rule ( 0 )
# ( Xi ) is the initial point
# If The Equation was set to "0" you need to provide The Values First Derivative ( dr ) And Second Derivative ( Ddr ). if not selected keep 0
# If The Equation was set to "1" you need to provide The Equation in the function ( F ) if not selected keep 0
# ( n ) is the number of Iterations needed

Equation = 1

Xi = 8.6                  

dr = 1.2                 

Ddr = 5                   

def F(x): return -0.25*x**4+1.1*x**3-1.75*x**2+2*x

n = 5

print("\n-----------------------------------------------------------------")
print(" Iteration |   Xi    |   F(Xi)  |   F(x)\'  |  F(x)\"    |  Error "
      "\n-----------------------------------------------------------------")
Error = 100
XiPlus1 = 0
for i in range (n):
    if Equation == 1:
        print("\t{0:1d}  | {1:.5f} | {2:.5f}  | {3:.5f} | {4:.5f} |  {5:.4f}%\n"
              .format(i, Xi, F(Xi), derivative(F, Xi, dx=1e-6), derivative(F, Xi, dx=1e-6, n = 2 ), Error)) 
        XiPlus1 = Xi - derivative(F, Xi, dx=1e-6)/derivative(F, Xi, dx=1e-6, n = 2 )
        Error = abs(((XiPlus1 - Xi)/XiPlus1) *100)
    if Equation == 0:
        print("\t{0:1d}  | {1:.5f} |  F(Xi)  | {2:.5f} | {3:.5f} |  {4:.4f} %\n"
              .format(i, Xi, dr2,Ddr2, Error)) 
        XiPlus1 = Xi - (dr/Ddr)
        Error = abs(((XiPlus1 - Xi)/XiPlus1) *100)
        if i == 2 : break
    Xi = XiPlus1
    
# Finally displaying the solution as well as the percentge of error after each iteration
