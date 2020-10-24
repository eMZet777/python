"""
Stworz funkcje  generujaca  w nieskonczonosc  kolejne  liczby przemnozone
przez siebie  tzn.:

1
4
9
16
25
36
49
64
81
itd

skozystaj z funkcji generujacej  genrujac  20 elementow,
po czym  wroc od  momentu skonczenia i  wygeneruj  nastepne  30 kolejnych  liczb.

zapisz  wygeberowane  elementy w  tej  smaje liscie .
"""

"""

moje zadanie
def generate_numbers_multiplied_by_itself():
    for x  in  range(20):
        wynik = x*x
        yield wynik
        x +=1

print(list(generate_numbers_multiplied_by_itself()))

"""


def number_multiplied_by_itself_generator():
    number = 0
    while True:
        number = number + 1
        yield number * number

generatedNumbers = []

numberGenerator = number_multiplied_by_itself_generator()

for _ in range(20):
    generatedNumbers.append(next(numberGenerator))

print(generatedNumbers)

"""

"""
for _ in range(30):
    generatedNumbers.append(next(numberGenerator))

print(generatedNumbers)    
