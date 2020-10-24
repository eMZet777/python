""""
    czy:   /EL. UNIKALNE    /KOLEJNOSC  /ZMIANA KONKRETNEGO EL. /NOWE ELEMENTY
list          NIE              TAK          TAK                       TAK
krotki        NIE              TAK          NIE                       NIE
slowniki      TAK              NIE          TAK                       TAK
zbiory        TAK              NIE          NIE                       TAK

                ZBIORY: BONUS w postaci |&-^

"""

A = {1, 4, 20, -4, 20}

B = {1, 4, 5}

"""

A.add(7)


print (A)


funkcja set  zamienia liste  w zbior  i usowa  duplikaty

print(set(A))

"""
print(A&B) # (koniunkcja zbiorow) funkcja pokoazujaca  wspolne elementy  w zbiorach  A i  B

print (A|B) # (suma zbiorów) funkcja pokazuje wszystkie elementy w  zbiorze A i B ale kolejnosc wynikow nie jest  zachowana 


print (A-B) # odejmujemy  A-B i pokazuje co zostalo w zbiorze  A ( nie ma ich  w  B)

print (B-A) # odejmujemy B-A i pokazuje co zostalo w zbiorze B (nie ma ich  w  zbiorze A)
 
print (A^B) # alternatywa wylkuczajaca pokazuje o  co nie jest czescia wspolna (A&B)


# elementy mozna  usunac
A.discard(24)
print(A)

# spawdzanie czy  czy  A podzbiorem  zbioru  A

print (A.issubset(B))
print (B.issubset(A))





