# The Below Code Calculates X using Newton's Method

from scipy.misc import derivative

####################################### FOR Single Iterations #################################################        

def F1(x):
    return 2*x * m.cos(2*x) - 3 * m.cos(5*x) + 2*x  

    
    #  m.sin(0.2)
    #  m.cos(0.2)
    #  m.tan(0.2)
    #  m.pow(1, 2)   Square
    #  m.pow(1, 0.5)  Redical
    #  m.exp(2) 
    

xi = 0.5


Xiplus1 = xi - derivative(F1, xi, dx=1e-6)/derivative(F1, xi, dx=1e-6, n = 2 )
print("\n\n Xi = " , xi)
print("\n F(Xi) = " , F1(xi))
print("\n F(X)\' =", derivative(F1, xi, dx=1e-6))
print("\n F(X)\" =", derivative(F1, xi, dx=1e-6, n = 2 ))
print("\n Xi+1 =", Xiplus1)

###############################################################################################################

####################################### FOR N Number of Iterations ############################################


def F2(x):
    return 2*x * m.cos(2*x) - 3 * m.cos(5*x) + 2*x  

Xi = 0.5


print("\n Iteration |   Xi    |   F(Xi)  |   F(x)\'  |  F(x)\"    |  Error "
      "\n--------------------------------------------------------------------")
count = 0
Error = 0
XiPlus1 = 0
for i in range (0, 6):
    
    print("\t{0:1d}  | {1:.5f} | {2:.5f}  | {3:.5f} | {4:.5f} |  {5:.5f}\n"
          .format(count, Xi, F2(Xi), derivative(F2, Xi, dx=1e-6), derivative(F2, Xi, dx=1e-6, n = 2 ), Error)) 
    
    XiPlus1 = Xi - derivative(F2, Xi, dx=1e-6)/derivative(F2, Xi, dx=1e-6, n = 2 )
    Error = abs(((XiPlus1 - Xi)/XiPlus1) *100)
    Xi = XiPlus1
    count +=1
    
    
    
