"""Задача 4: Разработка контекстного менеджера для работы с файлами
Создай контекстный менеджер для работы с файлами, который будет автоматически
открывать и закрывать файл, а также обрабатывать возможные исключения.
Используй магические методы enter и exit"""


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


# Пример использования
with FileManager("example.txt", "w") as file:
    file.write("Hello, world!")
