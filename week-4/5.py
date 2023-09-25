def printPoly(p_x):
    term = len(p_x) - 1
    polyStr = "P(x) = "

    for _ in range(len(px)):
        coef = p_x[_]
        if coef == 0: continue
        if (coef >= 0 and _ != 0):
            polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + " "
        term -= 1
    
    return polyStr

def calcPoly(xVal, p_x):
    retValue = 0
    term = len(p_x) - 1

    for _ in range(len(px)):
        coef = p_x[_]
        retValue += coef * xVal ** term
        term -= 1

    return retValue

px = [7, -4, 0, 5]

print(printPoly(px))
xValue = int(input("X 값 --> "))
print(calcPoly(xValue, px))