# TYPY ZAGNIEZDZONE

imie = "Arkadiusz"
wiek = 29
plec = "mezczyzna"

imie2 = "Wioletta"
wiek  = 23
plec = "kobieta"

#krotki :

osoba1 = ('Arkadiusz', 29, 'mezczyzna')
osoba2 = ('Wioleta', 23, 'kobieta')
osoba3 = ('Kuba', 33, 'mezczyzna')


# rozwiazanie poprzez typy zagniezdzone jak nizej poprzez listy"

"""
listaGosci = [
                ['Arkadiusz', 28, 'mezczyzna'],
                ['Wioletta', 23, 'kobieta'],
                ['Kuba', 32, 'mezczyzna']
             ]

# teraz podmieniamy wartosc wieku Arkadiusza

listaGosci[0][1] = 29

"""
"""
#lista gosci moze byc jako krotka i wtedy dziala szybciej


listaGosci = [
                ('Arkadiusz', 28, 'mezczyzna'),
                ('Wioletta', 23, 'kobieta'),
                ('Kuba', 32, 'mezczyzna')

             ]
#mozna dodawac lite gosci ale nie zmianiamy wewnetrzych elementow
 
listaGosci.append(('Karol', 26, 'mezczyzna'))
"""

"""
listaGosci = {
                ('Arkadiusz', 28, 'mezczyzna'),
                ('Wioletta', 23, 'kobieta'),
                ('Kuba', 32, 'mezczyzna')

             }


listaGosci.add(('Karol', 26, 'mezczyzna')) #do dlownika dodajemy przez add ale bez kolejnosci 
""""

listaGosci = {
                ('Arkadiusz', 28, 'mezczyzna'),
                ('Wioletta', 23, 'kobieta'),
                ('Kuba', 32, 'mezczyzna')

             }

listaGosci2 = {
                ('Arkadiusz', 28, 'mezczyzna'),
                ('W', 23, "kobieta '),
                ('K', 32, 'mezczyzna')

             }

listaGosci3 = listaGosci | listaGosci2

