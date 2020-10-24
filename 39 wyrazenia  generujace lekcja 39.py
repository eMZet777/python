import sys

evenNumbers = [element  # lista 
               for  element  in  range (400)
               if (element %2 = 0)
               ]

evenNumbersGenerator = (element  # generator
               for  element  in  range (400)
               if (element %2 = 0)
               )


# zadanie domowe  suam liczb  do  100 podniesionych  do  potego  w generatorze   

potega2generator = (element**2
                     for element  in  range (100)
                     )
"""
for  item in potega2generator:
    print(item)



print(sum(potega2generator))
    
"""

print(sys.getsizeof(potega2generator))

