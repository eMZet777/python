"""

OOP - Object Oriented Programming

Programowanie zorientowane wokół obiektów

OBIEKT

OBIEKTY - to pojemniki do przechowywania zmiennych i funkcji tematycznie ze
          sobą powiązanych do dalszego łatwiejszego ponownego użycia

Klasy   - foremki (szablony) do tworzenia egzemplarzy obiektów

Atrybut - cecha opisująca obiekt
Metoda - funkcja, która operuje na obiekcie


Instacja klasy - instance z ang. egzemplarz to obiekt, który wyszedł z formy (klasy)


"""


class User:
    age = 0


seba = User()
mirek = User()
arek = User()

mirek.age = 24

age = 40

print(seba.age)
print(mirek.age)
print(age)


x = 5
