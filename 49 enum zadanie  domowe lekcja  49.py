from enum import IntEnum

DzienTygodnia = IntEnum('DzienTygodnia', 'Poniedzialek Wtorek Sroda Czwartek Piatek Sobota Niedziela')

wybor  = int(input("""Wybierz dzien tygodnia:

1. Poniedzialek
2. Wtorek
3. Sroda
4. Czwartek
5. Piatek
6. Sobota
7. Niedziela
"""))

if(wybor == DzienTygodnia.Poniedzialek):
    print("Do Weekendu jeszcze 5 dni")

elif(wybor == DzienTygodnia.Wtorek):
    print("Do Weekendu jeszcze 4 dni")
    
elif(wybor == DzienTygodnia.Sroda):
    print("Do Weekendu jeszcze 3 dni")


elif(wybor == DzienTygodnia.Czwartek):
    print("Do Weekendu jeszcze 2 dni")

elif(wybor == DzienTygodnia.Piatek):
    print("Do Weekendu jeszcze 1 dzien")

elif(wybor == DzienTygodnia.Sobota):
    print("Pierwszy dzien weekendu")

elif(wybor == DzienTygodnia.Niedziela):
    print("Koniec Weekendu")

    
else:
    print("Nie ma takiego dnia")
