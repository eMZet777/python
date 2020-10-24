import figury


#enumeration - spis - wyliczenie

from enum import InEnum

Menu_Figury = InEnum('Menu_Figury', 'Kwadrat Prostokat Kolo Trojkat Trapez')

wybor = int(input("""Wybierz figure , torej  pole chcesz obliczyc:
1. Kwadrat
2. Prostokat
3. Kolo
4. Trojkat
5. Trapez
"""))


if (wybor  == Menu_Figury.Kwadrat):

    a = float(input("Podaj bok kwadratu: "))

    print("Pole  kwadratu wynosi: ", figury.pole_kwadratu(a))


elif (wybor == Menu_Figury.Prostokat):
    a = float(input("Podaj pierwszy bok prostokata: "))
    b = float(input("Podaj drugi bok prostokata: "))

    print("Pole prostokata wynosi: ", figury.pole_prostokata(a, b))


elif (wybor == Menu_Figury.Kolo):
    r = float(input("Podaj promoen  koła: "))
    
    print("Pole kola wynosi: ", figury.pole_kola(r))

elif (wybor == Menu_Figury.Trojkat):
    a = float(input("Podaj podstawe trojkata: "))
    h = float(input("Podaj wysokosc trojkata: "))

    print("Pole trojkata wynosi: ", figury.pole_trojkata(a, h))

elif (wybor == Menu_Figury.Trapez):
    a = float(input("Podaj pierwszy bok trapezu: "))
    b = float(input("Podaj drugi bok trapezu: "))
    h = float(input("Podaj wysokosc trapezu: "))

    print("Pole trapezu wynosi: ", figury.pole_trapezu(a, b, h))

else:
    print("nie podales prawidlowej  wartosci")





