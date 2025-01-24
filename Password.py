import itertools
import time

# Определяем диапазон символов для генерации пароля
characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

start_time = time.time()  # Запоминаем время начала выполнения программы

# Перебираем все возможные комбинации длины 4
for password in itertools.product(characters, repeat=4):
    # Конвертируем кортеж в строку
    password_str = ''.join(password)
    
    print(f"Проверяем пароль: {password_str}")
    
    # Проверка правильности пароля
    if password_str == '1234':
        end_time = time.time()
        
        print("Пароль найден!")
        print(f"Время подбора пароля: {(end_time - start_time):.2f} секунд")
        break
