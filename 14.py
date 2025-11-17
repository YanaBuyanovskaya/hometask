# 14. Напишіть лямбда-функцію, 
# яка перевіряє, чи є число додатним.

positive_num = lambda a: "Positive number"  if a > 0 else "It is a negative number or zero"

num = int(input("Enter a number: "))
print((positive_num(num)))


