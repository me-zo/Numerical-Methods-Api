import sympy as sp
from fastapi import APIRouter

from app.bisection.models import RequestBisectionModel, ResultBisectionModel, BisectionIterationModel
from app.shared_models import DescriptionModel

router = APIRouter(prefix="/bisection")

x, y, z = sp.symbols('x y z')


@router.post("/solve", response_model=ResultBisectionModel)
async def bisection_method(request: RequestBisectionModel):
    """
    Simply give the input needed as The following to approximate a math problem using Bisection Method:

        \n- X of The Lower Limit
        \n- X of The Upper Limit
        \n- F(x) the equation in terms of x
        \n- n The number of Iterations needed

    ### Example:
    * X lower = 1

    * X Upper = 5

    * Iteration Count = 5

    * F(x) = 2 * exp(-3 * x) + 3 * cos(5 * x) - x ** 2 + 5
    """

    def find_error(old, new):
        return abs((new - old) / new) * 100

    if request.round_to is None:
        request.round_to = 10
    result = ResultBisectionModel(Iterations=[], Count=request.count)
    function = sp.parse_expr(request.f_of_x.lower())

    old_xm = 0
    for i in range(request.count):
        x_m = (request.x_lower + request.x_upper) / 2
        error = find_error(old_xm, x_m)
        old_xm = x_m
        f_xl = function.subs(x, request.x_lower).evalf()
        f_xu = function.subs(x, request.x_upper).evalf()
        f_xm = function.subs(x, x_m).evalf()
        result.Iterations.append(
            BisectionIterationModel(id=i + 1, x_lower=round(float(request.x_lower), request.round_to),
                                    x_upper=round(float(request.x_upper), request.round_to),
                                    x_m=round(float(x_m), request.round_to),
                                    f_of_xl=round(float(f_xl), request.round_to),
                                    f_of_xu=round(float(f_xu), request.round_to),
                                    f_of_xm=round(float(f_xm), request.round_to),
                                    error_percentage=round(float(error), request.round_to)))
        print(result.Iterations)
        if f_xl * f_xm < 0:
            request.x_upper = x_m
        elif f_xl * f_xm > 0:
            request.x_lower = x_m

    print(result.__dict__)
    return result


@router.get("/description", response_model=DescriptionModel)
async def bisection_method():
    description = DescriptionModel(description="this method approximates solutions to math problems",
                                   tested_symbols=["sin", "cos", "tan", "cot", "exp", "other"])
    return description
