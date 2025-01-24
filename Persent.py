import random
sr_vs = []
what_persent = float(input('Какой процент?: '))
what_num = what_persent
for_ = 100

if what_persent < 1:
    what_persent = what_persent * 10
    for_ = for_ * 10


for i in range(0, 100000):
    attempts = 0
    while True:
        attempts += 1
        r = random.randint(0, for_)
        if r < what_num:  
            sr_vs.append(attempts)
            break
sr = sum(sr_vs) / len(sr_vs)
print(f"В среднем потребовалось {sr:.0f} попыток, чтобы выпало число 1.")
