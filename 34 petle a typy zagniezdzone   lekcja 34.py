# TYPY ZAGNIEZDZONE, wypisanie wartosci

imie = "Arkadiusz"
wiek = 29
plec = "mezczyzna"

imie2 = "Wioletta"
wiek  = 23
plec = "kobieta"



osoba1 = ('Arkadiusz', 29, 'mezczyzna')
osoba2 = ('Wioleta', 23, 'kobieta')
osoba3 = ('Kuba', 33, 'mezczyzna')




listaGosci = {
                ('Arkadiusz', 28, 'mezczyzna',999),
                ('Wioletta', 23, 'kobieta',998),
                ('Kuba', 32, 'mezczyzna',997)

             }

listaGosci2 = {
                ('Arkadiusz', 28, 'mezczyzna'),
                ('W', 23, 'kobieta'),
                ('K', 32, 'mezczyzna')

             }

listaGosci3 = listaGosci & listaGosci2

for imie, wiek, plec, nrTelefonu in listaGosci:
    print("imie: ", imie)
    print("wiek: ", wiek)
    print("plec: ", plec)
    print("nrTelefonu: ", nrTelefonu)
    print("\n") # grupuje  elementy i dodaje enter

