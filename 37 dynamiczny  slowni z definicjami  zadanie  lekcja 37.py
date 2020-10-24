"""
Napisz program, ktory pozwoli uzytkownikowi:
1) Dodawac nowe definicje
2) Szukac  istniejacych  definicji
3) Usuwac wybrane  przez niego definicje

"""


definicje ={}

while(True):


    print("1: Dodac definicje")
    print("2: Zanjdz definicje")
    print("3: Usun definicje")
    print("4: Zakoncz program")

    wybor = input("Co  chcesz zrobic: ")

    if (wybor =="1"):
        klucz = input("Podaj klucz (slowo) do  zdefiniowania; ")
        definicja = input("Podaj  definicje: ")

        definicje[klucz] = definicja
        print("Definicja  dodana  pomyslnie")
    elif (wybor == "2"):
        klucz = input("Czego szukasz? ")
        if klucz  in  definicje:
            print(definicje[klucz])
        else:
            print("nie znalziono definicji o nazwie", klucz)
    elif (wybor == "3"):
        klucz = input("Jaka  definicje  chcesz  usunac? ")
        if  klucz  in definicje:
            del(definicje[klucz])
            print("Usunieto definicje  o nazwie: ", klucz)
        else:
            print("Nie znaleziono definicji o nazwie: ", klucz)
    elif(wybor == "4"):
        print("Program ulegl  zakonczeniu")
        break
    else:
        print("Podales  wartosc  z  poza  zakresu ")
    
            
    
    
    


