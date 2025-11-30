from datetime import datetime
import random

def get_current_timestamp():
    return int(datetime.timestamp(datetime.now()))


class Expense:
    __id: int
    category: str
    sum: float
    created_at: str

    def __init__(self, category, sum):
        self.__id = get_current_timestamp() + random.randint(1,100)
        self.category = category
        self.sum = sum
        self.created_at = str(datetime.now())

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f"Expense ID: {self.id}\nCategory: {self.category}\nSumma: {self.sum}\nCreated at: {self.created_at}"


class Expense_Model:
    def __init__(self):
        self.__expenses = []

    def add_expense(self, expense:Expense):
        self.__expenses.append(expense)

    @property
    def expenses(self):
        return self.__expenses
    
    def get_expense(self, id:int)->Expense:
        if len(self.expenses) <=0: return None
        for exp in self.expenses:
            if exp.id == id:
                return exp
        return None
    
    def delete_expense(self, id):
        _exp = self.get_expense(id)
        if not _exp: return False
        self.expenses.remove(_exp)
        return True 
    
    def show_all_sum(self) ->float:
        total = 0.0
        for exp in self.expenses:
            total+=exp.sum
        return total



class Expense_View:
    def show_menu(self)->int:
        print("*"*30)
        print("1. Add new expense")
        print("2. Delete expense by id")
        print("3. Show list of expenses")
        print("4. Show sum of all expenses")
        print("5. Exit")
        print("*"*30)

        return int(input("Select menu item, enter value 1-5: "))
    
    def show_message(self, msg:str):
        print("\n")
        print("-"*30)
        print(msg)
        print("-"*30)
        print("\n")
    
    def create_expense(self)->Expense:
        category = input("Enter category for expense: ")
        sum = float(input("Enter sum of expense: "))
        return Expense(category,sum)
    
    def delete_expense(self, expenses:list[Expense])->int:
        self.show_expenses(expenses)
        return int(input("Choose expense for delete(enter id): "))
    
    def show_expenses(self, expenses:list[Expense]):
        for exp in expenses:
            print("-"*30)
            print(exp)
            print("-"*30)
    
    def show_exp(self):
        return int(input("Choose expense(enter id): "))
    
    def show_all_sum(self, total:float):
        print(f"All sum of expenses: {total}")
    

class Expense_Controller:
    def __init__(self, model:Expense_Model, view: Expense_View):
        self.__model = model
        self.__view = view
    
    @property
    def view(self): return self.__view

    @property
    def model(self): return self.__model

    def action_create(self):
        expense = self.__view.create_expense()
        self.__model.add_expense(expense)
        self.__view.show_message("Expense successfully created!")

    def action_delete(self):
        id = self.__view.delete_expense(self.__model.expenses)
        result = self.__model.delete_expense(id)
        if result:
            self.__view.show_message(f"Expense by id was successfully deleted!")
        else:
            self.__view.show_message(f"Expense didn`t delete! Try again!")
    
    def action_show_expenses(self):
        self.__view.show_expenses(self.model.expenses)
    
    def action_show_expense(self):
        id = self.__view.show_exp()
        exp = self.__model.get_expense(id)
        if not exp is None:
            self.__view.show_message(exp)
        else:
            self.__view.show_message("Expense is not exist!")
    
    def action_show_sum(self):
        total= self.__model.show_all_sum()
        self.__view.show_all_sum(total)

app = Expense_Controller(Expense_Model(), Expense_View())

while True:
    menu_item = app.view.show_menu()

    match menu_item:
        case 1:
            app.action_create()
        case 2:
            app.action_delete()
        case 3:
            app.action_show_expenses()
        case 4:
            app.action_show_sum()
        case 5:
            app.view.show_message("Exit!")
            break
        case _:
            app.view.show_message("Wrong choice! Try again!")
    