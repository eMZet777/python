"""
    Funkcja - to blok kodu do którego można odwołać się
              w każdej chwili, aby otrzymać pożądany przez nas wynik.

              definition - tworzenie funkcji

              def nazwa_funkcji ():
              instrukcja 1
              instrukcja 2

              nazwa_funkcji()

"""


def wiadomosc_powitalna(imie):

    print("Czesc", imie, "milo mi Cie widziec")

imiona = ("Marek", "Marta", "Karol")

for  imie  in imiona:
    wiadomosc_powitalna(imie)
    
"""

wiadomosc_powitalna("Marek")
wiadomosc_powitalna("Marta")
wiadomosc_powitalna("Karol")



print("Czesc Marek, milo mi Cie widziec.")
print("Czesc Marta, milo mi Cie widziec.")
print("Czesc Karol, milo mi Cie widziec.")


"""
