quadratic = input("enter your equation in the format: _x^2(+/-)_x(+/-)_")
pm = ("+","-")
quadraticy = input("Is your formula:"+" "+quadratic+" " +"(Y/N)")

if quadraticy == ("Y"):
    #fist goal is to find the first coefficient and label it A
    xsquared = int(quadratic.find("x^2"))
    coef1pos = slice(0,xsquared,1)
    a = float(quadratic[coef1pos])
    #next goal is to excerpt the second coefficient and label it B


    #now to  take the last coefficient and label it C
else:
    print("enter the equation in the correct syntax")

