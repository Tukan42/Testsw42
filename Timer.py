import time 
while True:
    what = input('Какой режим выберете секундоvер или таймер (1/2): ')
    a = 0.0
# секундомер
    if what == "1":
        
        num = float(input('До скольки будет секундомер?: '))
        num2 = int(num * 10)
        num3 = num2
        for i in range(num3 + 1):
            print(f'Время: {a:.1f} сек')
            a += 0.1
            time.sleep(0.1)
        print('Готово')
        
# таймер
    elif what == "2":
        num = input('Сколько по времени будет длиться таймер?: ')
        numm = int(num)
        num2 = int(num)
        num3 = 1
        for i in range(num2):
            print(f'Время: {numm:.1f} сек')
            numm -= 1
            time.sleep(1)
        print('0.0\nВремя вышло')
    else:
        print('Выбрано не провельное действие')
    go = input("хотите продолжить? (Y/N): ").upper()
    if go != 'Y':
        break
