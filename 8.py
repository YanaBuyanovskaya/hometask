# 8. Створіть словник із даними про співробітників 
# компанії (ім’я, посада, зарплата). Напишіть функцію, 
# яка сортує співробітників за зарплатою.

employeers = [
    {'name': 'Hanna', 'position': 'manager', 'salary': 30000},
    {'name': 'Kate', 'position': 'accountant', 'salary': 25000},
    {'name': 'Mark', 'position': 'director', 'salary': 70000},
    {'name': 'Jack', 'position': 'manager', 'salary': 20000},
    {'name': 'Nancy', 'position': 'cleaner', 'salary': 10000},
]

sortedBySalary = sorted(employeers, key = lambda x:x['salary'])

print("Employeers list sorted by salary: ")

for employeer in sortedBySalary:
    for key, value in employeer.items():
        print("{}: {}".format(key,value))