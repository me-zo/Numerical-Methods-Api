import math
import sympy as sp
x, y, z = sp.symbols('x y z')
sp.init_printing()

# To Identify if the input is an equation or only an application of the rule the below variable is used (1 for equation , 0 for non-equation)

Equation = 1

''' ^^^ CHECK THIS ^^^'''

X0 = 0.3  #if not equation then This Is a

XAt =  8.8 #if not equation then This Is x

# if the Var Equation Equals to 1 then the program will use the below function and the above two points as input

F = x**2*sp.exp(0.5*x+1)-x +2

# if the Var Equation Equals to 0 then the program will use the below List of function outputs as [f(x), f(x)', f(x)",....] and the above two points as input 

FxArr = [1.1,1.4,1.4]


if Equation == 1:
    print("  ___________________________________________________\n   Order |   Fx0    | Approx value |  Error"
      "\n  ---------------------------------------------------")
def Fact (f,valfact) :
    if valfact!= 0:  return (f/sp.factorial(valfact))*(XAt-X0)**valfact
    else :  return f.subs(x, X0).evalf()/sp.factorial(valfact)
def Error (val): return ((F.subs(x, XAt).evalf()-val)/F.subs(x, XAt).evalf())*100
Fx = F; Value = 0
for i in range(5):
    if Equation == 1:
        Value += Fact(Fx.subs(x, X0).evalf(),i)
        print("    {0:2d}   | {1:.4f} |    {2:.4f}  |  {3:.2f} % ".format(i,float(Fx.subs(x, X0)),float(Value),float(Error(Value))))
        drVal = sp.diff(Fx, x); drVal ; Fx = drVal
    if Equation == 0:
        if i == 0 : Value += FxArr[i]
        elif i < len(FxArr) :  Value += (FxArr[i]/sp.factorial(i))*(XAt-X0)**i
if Equation == 0:  print("\nThe value of f({0:.3f} ) at x = {1:.3f} is   {2:.5f}\n".format(float(XAt),float(X0), float(Value)))


# Finally The program prints the solution as well as the equation it used (if it used one)

F
