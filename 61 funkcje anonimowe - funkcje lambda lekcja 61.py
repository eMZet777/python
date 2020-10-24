"""

funkcje anonimowe  - funkcje bez nazwy - lambda

"""
def podwoj(x):
    return x*2

print(podwoj(4))


# lambda jest ok tylko dla jakis szybkich obliczen  bez dalszych odwolan
test = lambda x: x * 2
print((lambda x: x * 2)(4))

my_list = [2, 14, 22, 7, 6, 4, 5, 17] # filtrujemy liste na  przyste  i nieparyste aletylko raz

my_list_filtered = list(filter(lambda x: x % 2 == 0, my_list))
my_list_filtered2 = [   #lista wyrazeniowa
    x for x in my_list
    if (x%2) == 0
        ]

print(my_list_filtered)
print(my_list_filtered2)
