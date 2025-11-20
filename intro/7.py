# 7. Напишіть функцію, яка приймає список рядків і 
# повертає список, у якому рядки відсортовані за 
# довжиною.

def sort_by_length(words):
    return sorted(words, key=len)

myList = ['apple', 'pea', 'strawberry', 'cucumber']
sortedList = sort_by_length(myList)
print(sortedList)

