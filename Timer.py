import time

hur = int(input("Сколько часов будет длится таймер?: "))
minn = int(input("Сколько минут будет длится таймер?: "))
sec = int(input("Сколько секунд будет длится таймер?: "))

def timer(hours, minuts, seconds):
    total_sec = hours * 3600 + minuts * 60 + seconds
    
    
    for i in range(total_sec):
        h = total_sec // 3600
        m = (total_sec % 3600) // 60
        s = total_sec % 60
        
        print(f"Время: {h:02}:{m:02}:{s:02}")
        time.sleep(1)
        total_sec -= 1
timer(hur, minn, sec)
