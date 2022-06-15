# Here we simply give the input needed as The Following:
# ( X ) The Value of X that we would like to estimate the solution on
# ( Xarray ) and ( Yarray ) which are lists of the values that we want to work with
# if ( ArrayB ) is not empty then it is a list of the values that we to use in order to estimate F(x) 

X = 7

Xarray = [0, 4, 6]

Yarray = [2.3, 6.5, 14.2]

ArrayB = []  # Should Be EMPTY

print("\n\n-----------------------------------------------------------"
      "\n Iteration |     B     |     F    |    F'    |     Error  "
      "\n-----------------------------------------------------------")


def matrix_b(i):
    if i == 0:
        return Yarray[0]
    elif i == 1:
        return (Yarray[1] - Yarray[0]) / (Xarray[1] - Xarray[0])
    elif i == 2:
        return (((Yarray[2] - Yarray[1]) / (Xarray[2] - Xarray[1])) - (
                    (Yarray[1] - Yarray[0]) / (Xarray[1] - Xarray[0]))) / (Xarray[2] - Xarray[0])
    else:
        return 99999


def error(i):
    if i > 0:
        return abs((matrix_f(i) - Yarray[i]) / matrix_f(i)) * 100
    else:
        return 0


def matrix_f(i):
    if len(ArrayB) == 0:
        if i == 1: return matrix_b(i - 1) + matrix_b(i) * (X - Xarray[i - 1])
        if i == 2:
            return matrix_b(i - 2) + matrix_b(i - 1) * (X - Xarray[i - 2]) + matrix_b(i) * (X - Xarray[i - 2]) * (
                        X - Xarray[i - 1])
        else:
            return 0
    else:
        if i == 1: return ArrayB[i - 1] + ArrayB[i] * (X - Xarray[i - 1])
        if i == 2:
            return ArrayB[i - 2] + ArrayB[i - 1] * (X - Xarray[i - 2]) + ArrayB[i] * (X - Xarray[i - 2]) * (
                        X - Xarray[i - 1])
        else:
            return 0


def matrix_d(i):
    if i == 2 or i == 1:
        return matrix_b(i - 1) + matrix_b(i) * ((X - Xarray[i - 2]) + (X - Xarray[i - 1]))
    else:
        return 0


for i in range(len(Xarray)):
    B = matrix_b(i)
    f = matrix_f(i)
    fdr = matrix_d(i)
    print("     {0:1d}     |  {1:.4f}  |  {2:.4f} |  {3:.4f}  |  {4:.4f}% \n".format(i, B, f, fdr, error(i)))

# Finally, Displaying the solution as an iteration based format
