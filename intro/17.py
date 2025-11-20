# 17. Використовуючи лямбда-вираз і функцію filter, 
# знайдіть усі числа, 
# які діляться на 3, у списку чисел.

numbers = [3,1,66,34,231,99,21,7]
divisibleBy3 = list(filter(lambda x: x % 3 == 0, numbers))

print("Числа, які діляться на 3: ", divisibleBy3)