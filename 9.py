# 9. Використовуючи лямбда-вираз, створіть функцію, 
# яка повертає найбільше з двох чисел.

max_num = lambda a,b: a if a > b  else b

print(max_num(10,20))
print(max_num(30,12))