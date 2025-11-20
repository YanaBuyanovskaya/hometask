# 3. Створіть класи Book і Library, які будуть взаємодіяти між собою.
# Клас Book:
# назва  
# автор
# кількість сторінок
# ідентифікатор книги
# Методи:
# виводити інформацію про книгу

# Клас Library:
# список книг у бібліотеці
# Методи:
# використовуйте перевантажені операції:
# - додати книгу до бібліотеки 
# - видалити книгу за ідентифікатором
# шукати книгу за назвою та повертати її інформацію


class Book:

    def __init__(self, bookId ,name,author,count_pages):
        self.bookId = bookId
        self.name = name
        self.author = author
        self.count_pages = count_pages

    def __str__(self):
        return f"Book ID: {self.bookId}. Name of book is {self.name}. Author of this book is {self.author}. Count of pages of {self.name} is {self.count_pages}."
    
    def book_info(self):
        return(f"ID: {self.bookId}\n Name: {self.name}\n Author: {self.author}\n Count pages: {self.count_pages}")
  

class Library:
    def __init__(self):
        self.books: list[Book] = []

    def __add__(self, book:Book):
        for b in self.books:
            if b.bookId == book.bookId:
                raise ValueError(f"Book with ID {book.bookId} is in library already.")
        self.books.append(book)
        return self
    
    def __sub__(self,book_id):
        
        new_books = [b for b in self.books if b.bookId !=book_id]

        if len(new_books) == len(self.books):
            print(f"Book with ID {book_id} was not find in library.")
        else:
            print(f"Book with ID {book_id} was removed.")

        self.books = new_books
        return self
    
    def find_by_name(self, name):
        for book in self.books:
            if book.name == name:
                return book.book_info()
            else:
                return f"Book with name {name} does not exist in library."
            
    def print_info(self):
        if not self.books:
            print("Library is empty.")
        else:
            for book in self.books:
                print(book)




book1 = Book(1, "Чистий код", "Роберт Мартін", 447)
book2 = Book(2, "Сам себе программист", "Кори Альтхофф", 207)
# print(book1)

lib = Library()
lib = lib + book1
lib = lib + book2

print("Our library: ")
lib.print_info()

print("\nFind book by name: ")
print(lib.find_by_name("Чистий код"))
print(lib.find_by_name("Unknown book"))

print("\nRemove book with ID 2: ")
lib = lib - 2

print("Library after removing book...")
lib.print_info()

