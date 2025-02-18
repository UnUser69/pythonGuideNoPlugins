def printAnything():
    thing = input('Напишите строку состоящую только из букв: ')
    alphaCheck = thing.isalpha()
    if alphaCheck == True:
        print('Это строка состоящая только из букв.')
    else:
        while alphaCheck == False:
            thing = input(f'Напишите строку состоящую только из букв!\n:::')
            alphaCheck = thing.isalpha()
        print('Это строка состоящая только из букв.')

def printColores():
    words = ['Welcome', 'to', 'python']
    print(words)
    print(*words, end="!\n")
    print(*words, sep="\n")
    with open("output.txt", "w", encoding="utf-8") as f:
        print("Эту строку Python запишет в файл output.txt", file=f)
        print("Вторая строка тоже будет в файле", file=f)
    print("Эту строку Python напечатает моментально", flush=True)

def lenInWork():
    cats = ['Red', 'Bob', 'Coat']
    tuple = ('Red', 'Bob', 'Coat')
    dictionaryBitch = {'a':1, 'b':2}

    print(len(cats))                                        #RESULT: 3
    print(len(tuple))                                       #RESULT: 3
    print(len(dictionaryBitch))                             #RESULT: 2
    print(len('марк'))                                      #RESULT: 4
    print(len('м2рк'))                                      #RESULT: 4
    #print(len(2))                                          #RESULT: TypeError: object of type 'int' has no len()
    #print(len(2.23))                                       #RESULT: TypeError: object of type 'float' has no len()
    #print(len(False))                                      #RESULT: object of type 'bool' has no len()

def strInWork():
    #strList = [10, 10, 10]                                 #RESULT: TypeError: sequence item 0: expected str /n
                                                            # instance, int found
    strList = ['10', '10', '10']
    print(','.join(strList))                                #RESULT: 10,10,10

    print('gOg1'.upper())                               #RESULT: GOG1 1 при использовании аргумента UPPER не /n
                                                        # заменяет ее на !
    print('gOg1'.lower())                               #RESULT: gog1
    print('gOg1'.swapcase())                            #RESULT: GoG1
    print('gOg1'.capitalize())                          #RESULT: Gog1
    print('gOg1'.casefold())                            #RESULT: gog1
    print("Homer Simpson".swapcase())  # RESULT: hOMER sIMPSON


    print('gOg1'.center(12, "-"))        #RESULT: ----gOg1----
    print('gOg1'.isalnum())                             #RESULT: True
    print('gOg1'.isalpha())                             #RESULT: False
    print('gOg1'.isdecimal())                           #RESULT: False
    print('gOg1'.isdigit())                             #RESULT: False
    print('gOg1'.isidentifier())                        #RESULT: True
    print('gOg1'.islower())                             #RESULT: False
    print('gOg1'.isnumeric())                           #RESULT: False
    print('gOg1'.isprintable())                         #RESULT: True
    print('gOg1'.isspace())                             #RESULT: False
    print('gOg1'.istitle())                             #RESULT: False
    print('gOg1'.isupper())                             #RESULT: False
    print('gOg1'.join("USA"))                           #RESULT: UgOg1SgOg1A
    #print('gOg1'.ljoin("USA"))                          #AttributeError: 'str' object has no attribute 'ljoin'. Did you mean: 'join'?
    print('gOg1'.lstrip("USA"))                         #RESULT: gOg1
    print("Tea bag. Tea cup. Tea leaves.".replace("Tea", "Coffee"))     #RESULT: Coffee bag. Coffee cup. Coffee leaves.
    print("Tea bag. Tea cup. Tea leaves.".replace("Tea", "Coffee", 2))      #RESULT: Coffee bag. Coffee cup. Tea leaves.

    frm = "SecrtCod"
    to = "12345678"
    trans_table = str.maketrans(frm, to)
    secret_code = "Secret Code".translate(trans_table)
    print(secret_code)                                      #RESULT: 123425 6782

    print("Yes Fitness".rfind("Y"))                         #RESULT: 0
    print("Yes Fitness".rfind("Homer"))                     #RESULT: -1
    print("Yes Fitness".rindex("Y"))                        #RESULT: 0
    #print("Yes Fitness".rindex("Homer"))                        #ValueError: substring not found
    print("bee".rjust(12, "-"))             #RESULT: ---------bee
    print("Homer-Jay-Simpson".rpartition("-"))              #RESULT: ('Homer-Jay', '-', 'Simpson')
    print("Homer-Jay-Simpson".rsplit(sep="-", maxsplit=1))      #RESULT: ['Homer-Jay', 'Simpson']
    print("-----Bee-----".rstrip("-"))                      #RESULT: -----Bee
    print("Tea\n\nand coffee\rcups\r\n".splitlines(keepends=True))      #RESULT: ['Tea\n', '\n', 'and coffee\r', 'cups\r\n']
    print("Tea\n\nand coffee\rcups\r\n".splitlines(keepends=False))     #RESULT: ['Tea', '', 'and coffee', 'cups']
    print("36".zfill(5))                                    #RESULT: 00036
    print("36".zfill(5).replace("3", "X"))      #RESULT: 000X6


    string1 = 'interface FastEthernet0/1'
    print(string1.find('Fast'))                             #RESULT: 10 (поиск слева)!!!Чувствителен к регистру!!!
    print(string1[string1.find('Fast')::])                  #RESULT: FastEthernet0/1 (поиск слева)!!!Чувствителен к регистру!!!
    print(string1.rfind('Fast'))                            #RESULT: 10 (поиск справа)!!!Чувствителен к регистру!!!
    print(string1[string1.rfind('Fast')::])                 #RESULT: FastEthernet0/1 (поиск справа)!!!Чувствителен к регистру!!!
    print(string1.startswith('Fast'))                       #RESULT: True Чувствителен к регистру!!!
    print(string1.startswith('fast'))                       #RESULT: False Чувствителен к регистру!!!
    print(string1.endswith('0/1'))                          #RESULT: True Чувствителен к регистру!!!
    print(string1.endswith('0/2'))                          #RESULT: False Чувствителен к регистру!!!
    print(string1.replace('Fast', 'Gigabit'))   #RESULT: 'FastEthernet0/1' --> 'GigabitEthernet0/1'

