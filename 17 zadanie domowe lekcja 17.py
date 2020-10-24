z = input( " + dodawanie,  - odejmownie, / dzielenie, * mnozenie ")

a = int(input("podaj pierwsza liczbe "))
b= int(input( "podaj  druga liczbe "))

if (z == "+"):
    print (a+b)
elif (z == "-"):
    print(a-b)
elif (z == "*"):
    print(a*b)
elif (z == "/"):
    if (b==0):
        print("Nie dzielimy  przez zero")
    else:
        print(a/b)
else:
    print ("nie wykonales  dobrego  wyboru")
