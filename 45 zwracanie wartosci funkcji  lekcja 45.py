""" return - zwroc"""

def pole_prostokata(a, b):
    return(a*b)

print(5*pole_prostokata(2,8))

print(pole_prostokata(3,10))

def dzielenie(a, b):
    if ( b == 0):
        return
    
    return a/b


x = dzielenie (10,5)

if(x):
    print("podzielono poprawnie", x)

else:
    print("cos poszlo nie tak")
