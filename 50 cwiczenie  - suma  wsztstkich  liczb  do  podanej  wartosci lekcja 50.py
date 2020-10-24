"""
Napisz  program, ktory policzy ume wszystkich  liczb od do podanej  liczby

dla  np  5
1+2+3+4+5
zwroci
15

range(6)
1,2,3,4,5

"""

"""

# opcja  - rozwiazanie z  petla 

suma = 0
for  liczba  in  range(1,6):
    suma = suma + liczba

print(suma)


"""

# opcja  1  - poprzez  definicje


def sumuj_do(liczba):
    suma = 0
    
    for  liczba  in  range(1,liczba+1):
        suma = suma + liczba

    return suma

print(sumuj_do(25))



# opcja 2  opprzez definicje


def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1,liczba+1)]) # lista

def sumuj_do3(liczba):
    return sum({liczba for liczba in range(1,liczba+1)}) # set

def sumuj_do4(liczba):
    return sum((liczba for liczba in range(1,liczba+1))) # generator

print(sumuj_do2(25))
print(sumuj_do3(25))
print(sumuj_do4(25))


# opcja 3 poprzez definicje

def sumuj_do5(liczba):
    return(1 + liczba) / 2 * liczba

print(sumuj_do5(25))


    
