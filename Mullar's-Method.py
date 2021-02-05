import sympy as sp
x, y, z = sp.symbols('x y z')
sp.init_printing()

# Here we simply give the input needed as The Following:
# ( X0 ) & ( X1 ) & ( X2 )
# ( Fx ) is the equation of the function 
# ( n ) is the number of Iterations needed

x0 = 4.5

x1 = 5.5

x2 = 5

Fx = x**3 - 13*x - 12

n = 3

print("____________________________________________________________________________________________________________\n  "
      "Iteration |    X3    |    H0   |    H1    |    D0    |    D1   |    A    |    B    |    C    |   Error  "
      "\n------------------------------------------------------------------------------------------------------------")
for i in range(n):
    # Finding F(x0) & F(x1) & F(x2)
    fx0 = Fx.subs(x, x0).evalf(); fx1 = Fx.subs(x, x1).evalf(); fx2 = Fx.subs(x, x2).evalf(); 
    # Finding H 0 & 1
    H0 = x1 - x0; H1 = x2 - x1; 
    # Finding Delta 0 & 1 
    d0 = (fx1 - fx0)/(x1 - x0); d1 = (fx2 - fx1)/(x2 - x1); 
    # Finding A & B & C
    A = (d1 - d0)/(H1 + H0); B = A*H1 + d1; C = fx2;
    # To Calculate X3 we have two solutions one is when delta is positive and the other is when its negative
    DeltaPos = (B + sp.sqrt(B**2 - (4*A*C)))
    DeltaNeg = (B - sp.sqrt(B**2 - (4*A*C)))
   
    if (abs(DeltaPos) > abs(DeltaNeg)): x3 = x2 + ((- 2*C)/DeltaPos)
    else: x3 = x2 + ((- 2*C)/DeltaNeg)
    Error = abs(((x3 - x2)/x3)*100)
    print("     {0:2d}     |  {1:.5f} | {2:.5f} | {3:.5f} | {4:.5f} | {5:.4f} | {6:.4f} | {7:.4f} | {8:.4f} | {9:.6f} \n"
      .format(i+1, x3, H0, H1, d0, d1, A, B, C, Error))
    # Changing Variables for The Next Iteration
    x0 = x1; x1 = x2; x2 = x3; 
 
# Finally displaying the output with the value of every rule that was needed in order to get the final answer and the percentage of error after each iteration
