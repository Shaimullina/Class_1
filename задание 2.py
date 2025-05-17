"""Задача 2: Создание банковской системы
Создай систему для управления банковскими счетами. У каждого счета должны быть атрибуты: номер счета, имя владельца, баланс. Система должна поддерживать следующие операции:
1. Депозит средств.
2. Снятие средств.
3. Проверка баланса.
4. Перевод средств с одного счета на другой.
Используй магические методы для вывода информации о счете и для проверки равенства счетов (например, по номеру счета)
"""


class BankAccount:
    def __init__(self, account, name, balance):
        self.account = account
        self.name = name
        self.balance = balance

    def add_account(self, account):
        self.account = add_account
        add_account = []
        self.account.append(account)


class BankSystem:
    def __init__(self, amount):
        self.amount = amount

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} Депозит {amount} руб. Текущий баланс: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.name} Вывести {amount} руб. Текущий баланс: {self.balance}")
        else:
            print("Недостаточно средств.")


# Пример использования
account1 = BankAccount("12345", "Иван Иванов", 1000)
account2 = BankAccount("67890", "Петр Петров", 2000)
bank = BankSystem(345)
bank.add_account(account1)
bank.add_account(account2)
account1.deposit(500)
account2.withdraw(300)
bank.transfer("12345", "67890", 200)
print(account1)
print(account2)
