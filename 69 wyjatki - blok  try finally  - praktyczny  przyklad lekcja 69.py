"""
PLIK - nazwana lokacja, która przechowuje na STAŁE dane na dysku.

RAM - pamięć podręczna komputera, gdzie przechowywane są dane TYMCZASOWO

Operacje na plikach
1) otwieranie
2) pisanie/czytanie
3) zamykanie

podstawowe sposoby otwierania plików
r - R ead (czytanie) - domyślne
w - W rite (pisanie) - jeślli plik istniał to go usunie,
                        jeśli nie to stworzy
a - A ppend (dopisywanie)

rozszerzenie to tylko 'tekst' nadawany po to, aby inne programy
             rozpoznawały plik w odpowiedni dla tych programów sposób


"""

try:

    file = open ("test.txt", "w") # UCHWYT HANDLE 
    file.write("Sample")

    print(0/0)
    a = 5
    file.write("Sample")

finally:
    file.close()
    a =5
    
