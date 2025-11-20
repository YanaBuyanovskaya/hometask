# 13. Створіть кортеж із кількох чисел. 
# Напишіть функцію, яка знаходить суму всіх чисел у кортежі.

myTuple = (1,2,3,4,5)

def sum_tuple(numbers):
    sum = 0
    for i in numbers:
        sum+=i
    return sum

print("Сума чисел кортежу: ", sum_tuple(myTuple))