"""

wyrazenie  slownikowe

"""

names = {"Arkadiusz", " Wioletta", "Karol", "Bartlomiej", "Jakub",  "Ania"}

numbers = [1, 2, 3, 4, 5, 6]


celcius = {"tl": -20, "t2": -15, "t3": 0, "t4": 12, "t5": 25}

"""
namesLenght = {
    name : len(name) # co sie stanie z kluczam i  wartosciami w slowniku(krok 1)
    for name in names # skad  pobieramy elementy(krok 2)
    if name.startswith("A") # warunek jesli potrzebny jest (krok 3)

}
"""              
"""
multipliedNumbers = {
    number : number*number
    for  number in numbers
    }

"""
"""

multipleNmbers**2 = {
    number : number**2
    for number in numbers
            }

multipleNumbers**3 = {
    number : number*3
    for  number in numbers
    }
"""

farenheit = {
    key: celcius *1,8 + 32
    for key, celcius in celcius.items():
    }


