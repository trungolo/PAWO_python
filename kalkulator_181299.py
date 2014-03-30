def RepresentsFloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

def ReplaceWithProperValues(indexes,chars):
    #Powoduje zmiane postaci ogolnego wyrazenia, np. dla "+ * 2 3 + 1 4", bedzie ono przyjmowalo taka postac:
    #Krok 1: + 6 + 1 4
    #Krok 2: + 6 5
    #Krok 3: 11
    while len(indexes) >0:
        a = indexes.pop()
        b = float(chars[a+1])
        c = float(chars[a+2])
        if chars[a] == "+":
            d = b + c
        elif chars[a] == "-":
            d = b - c
        elif chars[a] == "*":
            d = b * c
        else:
            d = b / c

        chars[a] = str(d)
        del chars[a+2]
        del chars[a+1] 

def Validation(chars):

    counter = 0
    index = 0

    #sprawdza, czy uzytkownik podal prawidlowe znaki (cyfry) oraz czy wyrazenie jest zgodne z notacja polska
    while counter <len(chars):
        #jezeli uzytykownik podal np. litere to konwersja na float wywola wyjatek
        if chars[counter] is not "+" and chars[counter] is not "-" and chars[counter] is not "*" and chars[counter] is not "/":
            isFloat = RepresentsFloat(chars[counter])

            if isFloat == False:
                raise
        else:
            #sprawdza czy roznica miedzy wartoscia indeksu najblizszych operatorow (+,-,*,/) sa mniejsze rowne 3, np. wyrazenie "+ 2 3 5 + 1 4" jest bledne bo nie wiadomo jak je zinterpretowac
            if counter - index <= 3:
                index = counter
            else:
                raise
        if counter == len(chars) -1:
            #sprawdza czy roznica miedzy wartoscia indeksu ostatniego operatora (+,-,*,/) a ostatnim indeksem w tablicy jest mniejsze rowne 2, np. wyrazenie "+ 2 3 + 1 4 5" jest bledne bo nie wiadomo jak je zinterpretowac
            if counter - index > 2:
                raise
        counter = counter + 1

def Operations():
    #UWAGA: Nalezy podawac znaki oddzielajac je spacja
    #Przyklad 1: + * 2 3 + 1 4 Wynik: 11
    #Przyklad 2: / 7 + 2 3 Wynik: 1.4

    expressions=[]
    results=[]

    flag = True
    while flag == True:
        var = raw_input("Podaj dzialanie do przeprowadzenia \r\nUWAGA! Liczby i operatory oddzielaj spacja\r\nK - koniec programu\r\n")
        if var != "K" and not var.startswith("save"):
            flag = True
            chars = []
            indexes = []
            counter = 0

            expressions.append("Wyrazenie: " + var)
            chars = var.split(" ")
            
            try:
                Validation(chars)

                while counter < len(chars):
                    if chars[counter] == "+" or chars[counter] == "-" or chars[counter] == "*" or chars[counter] == "/":
                        if chars[counter+1] == "+" or chars[counter+1] == "-" or chars[counter+1] == "*" or chars[counter+1] == "/":
                            indexes.append(counter +1)

                    counter = counter +1

                #Krok 1 - opis w funkcji ReplaceWithProperValues
                ReplaceWithProperValues(indexes,chars)
                counter  = 0
                while counter < len(chars):
                    if chars[counter] == "+" or chars[counter] == "-" or chars[counter] == "*" or chars[counter] == "/":
                        if RepresentsFloat(chars[counter+1]) and RepresentsFloat(chars[counter+2]):
                            indexes.append(counter)

                    counter = counter +1
    
                #Krok 2 - opis w funkcji ReplaceWithProperValues
                ReplaceWithProperValues(indexes,chars)
                counter  = 0
                while counter < len(chars):
                    if chars[counter] == "+" or chars[counter] == "-" or chars[counter] == "*" or chars[counter] == "/":
                        indexes.append(counter)

                    counter = counter +1

                #Krok 3 - opis w funkcji ReplaceWithProperValues
                ReplaceWithProperValues(indexes,chars)
                results.append("Wynik: " + chars[0])
                print "Wynik: " + chars[0] + "\r\n"
            except:
                results.append("Error")
                print "Blad: Podaj poprawne wartosci \r\n"
        elif var.startswith("save"):
            tab = []
            tab = var.split(" ")
            message = ""

            #Uzycie komendy save: "save <nazwa_pliku>"
            if len(tab) != 2:
                results.append("Error")
                print "Blad: Napisz komende save poprawnie \r\n"
            else:

                if(tab[1] != ""):
                    f = open(tab[1],"w")
                    counter = 0

                    while counter < len(expressions):
                         message = message + expressions[counter] + " " + results[counter] + "\r\n"
                         counter = counter + 1
                
                    f.write(message)
                    f.close()

                    print "Operacja zapisu zostala wykonana \r\n"
                else:
                    print "Blad: Podaj nazwe pliku \r\n"
        else:
            flag = False
Operations()


