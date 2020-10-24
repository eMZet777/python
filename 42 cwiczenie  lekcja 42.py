"""
Znajdź liczby od 2 do 470 włącznie, które są:
- podzielne przez 7, ale nie są podzielne przez 5

Z czego skorzystasz?
1) generatora
2) wyrażenia listowego
3) wyrażenia zbioru
4) wyrażenia słownikowego

Zastanów się, czy odpowiedź na to pytanie jest zawsze taka sama?

"""



# moje zadanie za pomoca generatora



liczbyzadanie = ( element
                 for element in range (100, 471)
                 if (element % 7 == 0 and element % 5 != 0)
                 )

print(liczbyzadanie)


# opcja za  pomoca wyrazenia zbioru



liczbyzadanie = [
                element
                for element in range (2, 471)
                if (element % 7 == 0 and element % 5 != 0)
                ]

print(liczbyzadanie)
