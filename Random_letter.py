
import random
import time

letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789                                                                                               ")

while True:
    letter = []
    for i in range(236):
        a = random.choice(letters)
        letter.append(a)
        res = ''.join(map(str, letter))
    print(res)
    
    time.sleep(0.1)
