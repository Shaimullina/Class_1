"""Задача 3: Управление сотрудниками
Создай систему для управления сотрудниками компании.
У каждого сотрудника должны быть атрибуты: имя, фамилия, должность, зарплата.
Система должна поддерживать наследование и полиморфизм для различных типов сотрудников
(например, менеджеры, разработчики, дизайнеры), и уметь рассчитывать бонусы для каждого типа сотрудников по разным правилам
"""


class Employee:
    def __init__(self, name, last_name, position, salary, plan):
        self.name = name
        self.last_name = last_name
        self.position = position
        self.salary = salary
        self.plan = plan


class Manager(Employee):
    def get_bonus(self, plan=7584, amount=1000):
        self.plan = plan
        if plan >= 2500:
            self.salary += amount
            print(
                f"Зарплата {self.name} была увеличена на {amount}, теперь она равна {self.salary}"
            )
        else:
            print(
                f"Зарплата {self.name} не увеличина, план не перевыполнен, она равна {self.salary}"
            )


class Developer(Employee):
    def get_bonus(self, plan=94749, amount=23000):
        self.plan = plan
        if plan >= 1278:
            self.salary += amount
            print(
                f"Зарплата {self.name} была увеличена на {amount}, теперь она равна {self.salary}"
            )
        else:
            print(
                f"Зарплата {self.name} не увеличина, план не перевыполнен, она равна {self.salary}"
            )


class Designer(Employee):
    def get_bonus(self, plan=500, amount=8765):
        self.plan = plan
        if plan >= 1400:
            self.salary += amount
            print(
                f"Зарплата {self.name} была увеличена на {amount}, теперь она равна {self.salary}"
            )
        else:
            print(
                f"Зарплата {self.name} не увеличина, план не перевыполнен, она равна {self.salary}"
            )


# Пример использования
employees = [
    Manager("Иван", "Иванов", "Менеджер", 100000, 1200),
    Developer("Петр", "Петров", "Разработчик", 80000, 1400),
    Designer("Анна", "Смирнова", "Дизайнер", 70000, 567),
]

for employee in employees:
    print(employee.get_bonus())
