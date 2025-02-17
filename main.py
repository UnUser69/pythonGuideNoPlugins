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
    strExemple = 'gOg1'                                     #RESULT: 1 при использовании аргумента UPPER не /n
                                                            # заменяет ее на !
    print(strExemple.upper())                               #RESULT: GOG1
    print(strExemple.lower())                               #RESULT: gog1
    print(strExemple.swapcase())                            #RESULT: GoG1
    print(strExemple.capitalize())                          #RESULT: Gog1
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

strInWork()