"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
"""
import random
n=int(input("Введите количество монет: "))
money=[]
up=0
down=0
for i in range(0, n):
    money.append(random.randint(0, 1))
    print(money[i], end=" ")
    if money[i]==0:
        down+=1
    else: up+=1
print()
if up>down:
    print(down)
else: print(up)

