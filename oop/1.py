# 1. Створіть клас Book, який має такі властивості:
# - назва книги
# - автор книги
# - кількість сторінок
# Додайте методи:
# -аксесори(властивості)
# -метод, який виводить інформацію про книгу
# -метод, який повертає True, 
# якщо кількість сторінок більша за 300, інакше False.

class Book:

    _name: str
    _author:str
    _count_page:int

    def __init__(self,name,author,count_page):
        self._name = name
        self._author = author
        self._count_page = count_page
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_value):
        if not new_value or len(new_value.strip())<=0:
            raise ValueError("new_value is none or empty")
        self._name = new_value
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_value):
        if not new_value or len(new_value.strip())<=0:
            return ValueError("new_value is none or empty")
        self._author = new_value

    @property
    def count_page(self):
        return self._count_page
    
    @count_page.setter
    def count_page(self,new_value):
        if not new_value or len(new_value.strip())<=0:
            return ValueError("new_value is none or empty")
        self._count_page = new_value


    def showInfo(self):
        print(f"The name of book {self._name}. Author of this book is {self._author}. This book has {self._count_page} pages.")
    
    def countMT300(self):
        if self._count_page > 300:
            print(True)
        else:
            print(False)
        

book1 = Book("Чистий код", "Роберт Мартін", 447)
book1.showInfo()
book1.countMT300()

book2 = Book("Сам себе программист", "Кори Альтхофф", 207)
book2.showInfo()
book2.countMT300()