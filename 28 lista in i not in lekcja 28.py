# in
# not in
# Opercje na  listach

imiona = ["Arkadiusz", "Wioletta", "Karol", "Kuba", "Adrian", "Wojtek"]
liczby = [2,12, 24, 7, -8]

print("Arkadiusz" in imiona)

if ("Arkadiusz" in imiona):
    print("Czesc Arek")

if(2 not in liczby):
    print("nie ma liczby 2")
else:
    print ("jest licba 2")

print(3*liczby)

print([4,20,15] + liczby)

liczby = [4,20,15] + liczby #przypisanie nowej wartosci listy (podmianka na zawsze)
