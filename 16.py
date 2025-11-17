# 16. Створіть кортеж із чисел і напишіть функцію, 
# яка знаходить найбільше і найменше значення в кортежі.

myTuple = (2,3,4,5,15,6,7,8,1,9,10)

def min_num(numbers):
    min_value = numbers[0]
    for i in numbers[1:]:
        if i < min_value:
            min_value = i
    return min_value

def max_num(numbers):
    max_value = numbers[0]
    for i in numbers[1:]:
        if i > max_value:
            max_value = i
    return max_value

print("Мінімальне значення кортежу: ", min_num(myTuple))
print("Максимальне значення кортежу: ", max_num(myTuple))