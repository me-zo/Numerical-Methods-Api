# Here we simply give the input needed as The Following:
# ( X ) The Value of xX that we would like to estimate the solution on
# ( Xarray ) and ( Yarray ) which are lists of the values that we want to work with
# if ( LArray ) is not empty then it is a list of the values that we to use in order to estimate F(x) 

X = 6.3               

Xarray = [-3,3,4,9]          

Yarray = [3.4,5,4.4,2]              

LArray = [] # SHOULD BE EMPTY else the Xarray will be ignored

if len(LArray) != 0 :
    print("\n\n-------------------------------------------------------------------"
        "\n     L     |  L(Value)   |      X      |      Y      |     Y(x)     "
        "\n-------------------------------------------------------------------")
def Matrix(X, Xi, Xl):
    return (X-Xl)/(Xi-Xl)
FOfx=0; res = 1; vall = 0
for L in range(len(Yarray)) :
    for i in range(len(Xarray)) :
        if Xarray[i] == 0 and Yarray[L] ==0: break
        if i!= L: res*=Matrix(X, Xarray[L], Xarray[i])
    if len(LArray) != 0 :
        FOfx += LArray[L]*Yarray[L]
        print("     {0:1d}     |   {1:.4f}    |   {2:.4f}    |   {3:.4f}    |    {4:.4f}  \n"
              .format(L , res , Xarray[L] , Yarray[L] , FOfx )) 
    else : 
        FOfx += res*Yarray[L]
        print("F( x ) = ",FOfx )
    res=1; vall+=1
# Finally Displaying the solution either as an iteration based format or as single line format depending on "LArray"
