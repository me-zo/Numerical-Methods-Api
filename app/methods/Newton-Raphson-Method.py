import sympy as sp

x, y, z = sp.symbols('x y z')
sp.init_printing()

# Here we simply give the input needed as The Following:
# ( Xi ) is The Initial Point  
# ( Fx ) is the equation of the function 
# ( n ) is the number of Iterations needed

Xi = 0

Fx = x ** 3 - 0.2589 * x ** 2 + 0.2262 * x - 0.001122

n = 5

print("\n_____________________________________________________")
print(" Iteration |   Xi    |   F(Xi)  |   F(x)\'  |  Error "
      "\n-----------------------------------------------------")
Error = 100
XiPlus1 = 0
for i in range(n):
    FxVal = float(Fx.subs(x, Xi).evalf())
    drFx = float(sp.diff(Fx, x).doit().subs(x, Xi).evalf())
    print("\t{0:1d}  | {1:.5f} | {2:.4f}  | {3:.4f}  | {4:.4f}%\n"
          .format(i + 1, Xi, FxVal, drFx, Error))
    XiPlus1 = Xi - FxVal / drFx
    Error = abs(((XiPlus1 - Xi) / XiPlus1) * 100)
    Xi = XiPlus1

# In The End The Program Prints The Output as well as The Percentage of error between Iterations
