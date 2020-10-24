def czytaj(file):
    try:
        with open ("file", "r", encoding="UTF-8") as file:
            return file.read()
    except FileNotFoundError:
        print ("nie znaleziono  pliku")

nazwaPliku = input("podaj nazwe pliku do otwarcia: ")

czytaj(nazwaPliku)
