# 10. Напишіть функцію, яка знаходить усі унікальні 
# елементи в списку і повертає їх у вигляді множини.

def unique_elem(smth_list):
    unique_list = list(set(smth_list))
    print(unique_list)

mySet = ['apple', 'apple', 145, 8, 'pear', 8]
print(unique_elem(mySet))