import sympy as sp
x, y, z = sp.symbols('x y z')
sp.init_printing()

# Here we simply give the input needed as The Following:
# ( Xl ) is X of The Lower Limit 
# ( Xu ) Is X of The Upper Limit 
# ( F ) is the equation of the function 
# ( n ) is the number of Iterations needed

Xl = 1

Xu = 5

F = 2*sp.exp(-3*x) + 3*sp.cos(5*x) - x**2 +5

n = 5

print(" __________________________________________________________________________________\n  "
      "Iteration |    Xl   |   Xu   |   Xm   |   F(Xl)  |  F(Xu)  |  F(Xm)  |    Error"
      "\n ----------------------------------------------------------------------------------")

def Error (old, new): return abs((new-old)/new)*100
Xm = 1 ;error = 0  ;oldXm = 0
for i in range(n):
    Xm = (Xl + Xu)/2
    error = Error(oldXm, Xm)
    oldXm = Xm
    Fxl = F.subs(x, Xl).evalf()
    Fxu = F.subs(x, Xu).evalf()
    Fxm = F.subs(x, Xm).evalf()
    print("      {0:2d}    |  {1:.4f} | {2:.4f} | {3:.4f} | {4:.4f} | {5:.4f} | {6:.4f} | {7:.3f} % "
          .format(i+1, float(Xl), float(Xu), float(Xm),float(Fxl),float(Fxu), float(Fxm), float(error)))
    if Fxl*Fxm < 0 :  Xu = Xm
    elif Fxl*Fxm > 0 :  Xl = Xm
    
# In The End The Program Prints The Output and specifies what the new Xm will be as well as The Percentage of error between Iterations
