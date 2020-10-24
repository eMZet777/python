"""

obiekt to  zmienn,  ktora  ma wiecej  mozliwosci,
mozna wywolac na  nim "funkcje"
moze miec wiecej  niz 1 wartosc

obiekty immutable : bool, int, float, tuple, str

immutable  - niezmienne
mutable - zmienne

= zmiana  miejsca wskazywania na  nowy adres, na  inny obiekt

"""




listSample = [1, 4, 512, 24]

listSample2 = listSample

listSample2.append(465)


a = 4
b = a
b = 7

k = 4
h = 4

c = 5

#print(id(c))
def add (c, amount = 1):
    print(id(c))
    c = c + amount
    print(id(c))
#add(c)
    """"

def append_element_to_list(listka, element):
    print(id(listka))
    listka.append(element)
    print(id(listka))
    
print(id(listSample))
append_element_to_list(listSample, 5)

"""

def append_element_to_list(listka, element):
    print(id(listka))
    a = [2, 4, 20]
    listka = a
    print(id(listka))
    
print(id(listSample))
append_element_to_list(listSample, 5)




