i = 0
wynik = 0

while  i < 3:

    x = int(input("podaj liczbe parzysta: "))
    if (x % 2 == 0 and x>0):
        wynik +=x
    else:
        print("miala byc  liczba parzysta; ")
        continue
    print("suma dodawania to: ", wynik)
    i +=1
