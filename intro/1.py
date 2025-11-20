#1. Створіть функцію, яка підраховує кількість цифр у числі
def count_innum():
    num = input("Enter a number: ")
    length = len(num)
    print(f"Length of your number: {num} = {length}")

print(count_innum())