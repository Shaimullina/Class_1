""" "Задача 1: Создание библиотеки
Создай библиотеку для управления коллекцией книг. Каждая книга должна быть представлена как объект, содержащий атрибуты: название, автор, год издания, жанр и количество страниц.
Библиотека должна поддерживать следующие операции:
1. Добавление книги.
2. Удаление книги.
3. Поиск книги по названию.
4. Вывод всех книг одного автора.
5. Вывод всех книг, отсортированных по году издания.
Используй свойства для проверки корректности ввода данных (например, год издания должен быть положительным числом)
"""


class Book:
    def __init__(self, title, author, year, genre, pages):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages


class Library(Book):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book}' добавлена.")

    def search_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book

    def get_books_by_author(self, author):
        books_by_author = []
        for book in self.books:
            if book.author == author:
                books_by_author.append(book)
        return books_by_author

    def get_books_sorted_by_year(self):
        self.books.sort(key=lambda book: book.year)


# Пример использования
library = Library()
book1 = Book("Название1", "Автор1", 2001, "Жанр1", 300)
book2 = Book("Название2", "Автор2", 1999, "Жанр2", 150)
library.add_book(book1)
library.add_book(book2)
print(library.search_by_title("Название1"))
print(library.get_books_by_author("Автор1"))
print(library.get_books_sorted_by_year())
