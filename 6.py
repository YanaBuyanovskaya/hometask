# 6. Створіть кортеж із кількох рядків і чисел. 
# Напишіть функцію, яка повертає новий кортеж, що містить лише числа.

myTuple = tuple(('Alex', 12, 'John', 874, 'Helen', 55))


def numbers(myTuple):
    new_tuple = []
    for i in myTuple:
        if type(i) == int:
            new_tuple.append(i)
        else:
            continue
    return tuple(new_tuple)

new_tuple = numbers(myTuple)
print(new_tuple)
