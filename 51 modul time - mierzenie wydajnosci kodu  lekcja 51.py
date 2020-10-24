"""
Mierzenie wydajności skryptu
"""

import time

def sumuj_do(liczba):
    suma = 0
    
    for liczba in range(1,liczba+1):
        suma = suma + liczba        
        
    return suma

def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1,liczba+1)])

def sumuj_do3(liczba):
    return sum({liczba for liczba in range(1,liczba+1)})

def sumuj_do4(liczba):
    return sum((liczba for liczba in range(1,liczba+1)))

def sumuj_do5(liczba):
    return (1 + liczba) / 2 * liczba

start = time.perf_counter()
print(sumuj_do(256))
end = time.perf_counter()
print (end - start)
      

# definicja do liczenia czasu
def finish_timer(start):
    end = time.perf_counter()
    return end-start
    
start = time.perf_counter()
print(sumuj_do(256))
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do2(256))
print(finish_timer(start))


start = time.perf_counter()
print(sumuj_do3(256))
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do4(256))
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do5(256))
print(finish_timer(start))
