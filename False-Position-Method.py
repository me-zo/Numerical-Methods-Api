import math
import sympy as sp
x, y, z = sp.symbols('x y z')
sp.init_printing()

# Here we simply give the input needed as The Following:
# ( Xl ) is X of The Lower Limit 
# ( Xu ) Is X of The Upper Limit 
# ( F ) is the equation of the function 
# ( n ) is the number of Iterations needed

Xl = 1

Xu = 3

F = 2*sp.cos(x) +5*sp.sin(x) -2

n = 5

print(" ______________________________________________________________________________________\n  "
      "Iteration |     Xl   |    Xu   |   Xm   |   F(Xl)  |  F(Xu)  |   F(Xm)   |   Error"
      "\n --------------------------------------------------------------------------------------")
def Error (old, new):
    return abs((new-old)/new)*100
Xm = 1 ; error = 0 ; oldXm = 0
for i in range(n):
    Fxl = F.subs(x, Xl).evalf() ; Fxu = F.subs(x, Xu).evalf() ; Xm = Xu - (Fxu * (Xl - Xu))/(Fxl- Fxu)
    Fxm = F.subs(x, Xm).evalf() ; error = Error(oldXm, Xm); oldXm = Xm
    print("      {0:2d}    |  {1:.5f} | {2:.5f} | {3:.5f} | {4:.5f} | {5:.5f} | {6:.5f} | {7:.5f} % "
          .format(i+1, float(Xl), float(Xu), float(Xm),float(Fxl),float(Fxu), float(Fxm), float(error)))
    if Fxl*Fxm < 0 : Xu = Xm
    elif Fxl*Fxm > 0 : Xl = Xm
    
# In The End The Program Prints The Output and specifies what the new Xm will be as well as The Percentage of error is between Iterations

F
