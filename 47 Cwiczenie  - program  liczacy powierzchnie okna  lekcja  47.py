import math

print("1: Oblicz Pole prostokąta")
print("2: Oblicz pole  kwadratu")
print("3: Oblicz pole trojkata")
print("4: Oblicz pole trapezu")
print("5: Oblicz pole koła")

wybor = input("Pole jakiej figury chcesz  policzyc? ")

def pole_prostokata(a, b):
    return a * b

def pole_kwadratu(a):
    return a * a

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_trapezu(a, b, h):
    return (a + b) / 2 * h

def pole_trapezu2(a, b, h):
    print((a + b) / 2 * h)

def pole_kola(r):
    return math.pi * r ** 2

if (wybor == "1"):
    a = int(input("Podaj wartosc a:"))
    b = int(input("Podaj wartosc b: "))
    print(pole_prostokata(a, b))
    
elif (wybor == "2"):
    a = int(input("Podaj wartosc a:"))
    print (pole_kwadratu(a))

elif (wybor == "3"):
    a = int(input("Podaj wartosc a:"))
    h = int(input("Podaj wartosc h: "))
    print(pole_trojkata(a, h))

elif (wybor == "4"):
    a = int(input("Podaj wartosc a:"))
    b = int(input("Podaj wartosc b: "))
    h = int(input("Podaj wartosc h: "))
    print(pole_trapezu(a, b, h))

elif (wybor == "5"):
    r = int(input("Podaj wartosc r:"))
    print(pole_kola(r))

else:
    print("Nie wpisales liczby z zakresu od 1 do 5")

