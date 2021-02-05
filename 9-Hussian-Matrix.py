import sympy as sp
x, y = sp.symbols('x y')
sp.init_printing()

# Here we simply give the input needed as The Following:
# ( Equation ) First Specify if the input is an equation ( 1 ) or only a single application of the rule ( 0 )
# ( X ) and ( Y ) The initial Values
# If The Equation was set to "0" you need to provide The Values:
    # First Derivative in terms of X ( drX ).
    # First Derivative in terms of Y ( drY ).
    # Second Derivative of "drX" in terms of X ( drXX ).
    # Second Derivative of "drY" in terms of Y ( drYY ).
    # Second Derivative of "drX" in terms of Y ( drXY ) or the opposite.
    ############# if not selected you can keep 0 ###############
# If The Equation was set to "1" you need to provide The Equation ( F ). if not selected you can keep 0

Equation = 1

X = 10

Y = 6.1

drX = 0

drY =  0

drXX = -6.4

drYY = -6.6

drXY =  3.5

F =  9.8*x**7*y**3 - 9*x**2*y**8 +2.6*x + 5.6*y


if Equation == 1:
    drXVal = sp.diff(F, x).subs(x, X).subs(y, Y).evalf()
    drYVal = sp.diff(F, y).subs(x, X).subs(y, Y).evalf()
    drXXVal = sp.diff(sp.diff(F, x), x).subs(x, X).subs(y, Y).evalf()
    drYYVal = sp.diff(sp.diff(F, y), y).subs(x, X).subs(y, Y).evalf()
    drXYVal = sp.diff(sp.diff(F, x), y).subs(x, X).subs(y, Y).evalf()

if Equation == 0 : 
    drXVal = drX  
    drYVal = drY 
    drXXVal = drXX 
    drYYVal = drYY
    drXYVal = drXY
    
H = drXXVal*drYYVal - sp.Pow(drXYVal, 2)
HVal = H.subs(x, X).subs(y, Y)
GradVal = "Not Critical"
if HVal > 0 and drXXVal > 0 : print("\n  Local Min")
elif HVal > 0 and drXXVal < 0 : print("\n  Local Max")
elif HVal < 0 : print("\n  Saddle Point")

print("___________________________\n   Fx      | {0:.2f} " .format(float(drXVal)))  
print("___________________________\n   Fy      | {0:.2f} ".format(float(drYVal)))  
print("___________________________\n   Fxx     | {0:.2f} ".format(float(drXXVal)))  
print("___________________________\n   Fyy     | {0:.2f} ".format(float(drYYVal))) 
print("___________________________\n   Fxy     | {0:.2f} ".format(float(drXYVal))) 
print("___________________________\n   H       | {0:.2f} ".format(float(HVal))) 
print("___________________________\nGrad(ai)   | {0:.2f} ".format(float(drXVal))) 
print("___________________________\nGrad(bj)   | {0:.2f} \n".format(float(drYVal)))  

# Finally Displaying if The next point is a Critical point or not then the solution with each derivative
