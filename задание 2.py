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

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} Депозит {amount} руб. Текущий баланс: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.name} Вывести {amount} руб. Текущий баланс: {self.balance}")
        else:
            print("Недостаточно средств.")


class BankSystem(BankAccount):
    def __init__(self, name, accounts=[]):
        self.name = name
        self.accounts = accounts

    def add_account(self, account):
        self.accounts.append(account)

    def transfer(self, account_from, account_to, amount):
        if account_from.balance >= amount:
            account_to.withdraw(amount)
            account_from.deposit(amount)
            print("Деньги переведены")
        else:
            print("Ошибка перевода, проверьте баланс счета")


# Пример использования
account1 = BankAccount("12345", "Иван Иванов", 1000)
account2 = BankAccount("67890", "Петр Петров", 2000)
bank = BankSystem(456)
bank.add_account(account1)
bank.add_account(account2)
account1.deposit(500)
account2.withdraw(300)
bank.transfer(account1, account2, 200)
print(account1)
print(account2)
