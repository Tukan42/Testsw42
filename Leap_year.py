while True:
    # с чего и до куда
    year = int(input('С какого года вы хотите узнать все високосные года?:'))
    for_what = int(input('До кокого года будут записаны года (не всегда включительно)?:'))
    
    # проверка коректности
    
    if year > for_what:
        print('Год с которого вы будете узновать весокосные года не может быть меньше года до которого вы будете узновать года')
        go = input('Хотите начать с начала? (Y/N)').upper()
        if go not in ('Y', 'Н'):
            break
        
    elif for_what < 4:
        print('В промежутке между', year, 'и', for_what, "нет високосных годов")
        go = input('Хотите начать с начала? (Y/N)').upper()
        if go not in ('Y', 'Н'):
            break
    
        go = input('Хотите начать с начала? (Y/N)').upper()
        if go not in ('Y', 'Н'):
            break
    
    # вычесление годов
    print('\n\nкак то так')
    for year in range(year, for_what):
        if year % 4 == 0 and year % 100 != 0:
            print(year)
           
        elif year % 400 == 0:
            print(year)
            
        else:
            continue

    print('Готов :)')
    go = input('Хотите начать с начала? (Y/N)').upper()
    if go not in ('Y', 'Н'):
        break
