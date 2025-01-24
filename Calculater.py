while True:
    what = input('Какое действие будем делать? (-, +, *, /):')
    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))
    if what == '-':
        print(f'Ответ: {num1 - num2:.2f}')
    elif what == '+':
        print(f'Ответ: {num1 + num2:.2f}')
        
    elif what == '*':
        print(f'Ответ: {num1 * num2:.2f}')
    
    elif what == '/':
        if num2 == 0:
            print('Ошибка, на 0 делить нельзя')
        else:
            print(f'Ответ: {num1 / num2:.2f}')
    else:
        print("ошибка, выбрано  не веоное действие!")
    
    go = input('Хотите продолжить расчеты? (Y/N)').upper()
    if go not in('Y', 'Н'):
        break
