"""
Argumenty kluczowe  i pozycyjne
kluczowy - w  postaci: klucz - wartosc ( domyslny)
pozycyjne - takich, ktorych liczy sie  kolejnosc  przy wywolaniu

"""

def greet(name, message, separator=" "):
    print(message, name, sep=separator)

greet("Arek","Witojcie", "\n")
greet("Wiola", "\n")
