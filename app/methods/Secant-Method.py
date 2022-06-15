import sympy as sp

x, y, z = sp.symbols('x y z')
sp.init_printing()

# Here we simply give the input needed as The Following:
# ( Xi ) is the initial point  
# ( Xminus1 ) is the point before the Initial toint  
# ( Fx ) is the equation of the function 
# ( n ) is the number of Iterations needed

Xi = 0

Xminus1 = -0.5

Fx = sp.cos(x) + 2 * sp.sin(x) + x ** 2

n = 5

print("\n____________________________________")
print(" Iteration |    Xi     ||   Error "
      "\n------------------------------------")
Error = 0
XiPlus1 = 0
for i in range(n):
    FxVal = float(Fx.subs(x, Xi).evalf())
    FminusVal = float(Fx.subs(x, Xminus1).evalf())
    XiPlus1 = Xi - FxVal * (Xi - Xminus1) / (FxVal - FminusVal)
    Error = abs(((XiPlus1 - Xi) / XiPlus1) * 100)
    print("      {0:1d}    | {1:.6f} || {2:.6f}%\n"
          .format(i + 1, Xi, Error))
    Xminus1 = Xi
    Xi = XiPlus1

# In The End The Program Prints The Output as well as The Percentage of error between Iterations
