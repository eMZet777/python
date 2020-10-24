import sys

# wyrazenie lisowne  

evenNumbers = [element
               for element in range(400)
               if (element % 2 == 0)
               ]

# wyrazenie generujace - wypisujemy  dane  i o nich  zapominamy 

evenNumbersGenerator = (element
                        for element in range(400)
                        if (element % 2 == 0)
                        )
print(sys.getsizeof(evenNumbersGenerator))

for  item in evenNumbersGenerator:
    print(item)

potega2generator = (item**2
                    for  item in range (100)
                    )

print(sum(potega2generator))






                    
