"""
Code Duplicates Without Inheritance
Example:
- SavingsAccount -> interest_rate, balance -> add_interest(), deposit(), withdraw()
- CheckingAccount -> transaction_count, balance -> deduct_fees(), deposit(), withdraw()
-When multiple classes share similar attributes, you can reduce redundant code by defining a base class and then subclasses can inherit from the base class.
- Superclass: The more general class which hold the information of common features and behaviors.
- Subclass: The more specialized class that inherits from the superclass.

The "is a" Relationship
- The relationship between a superclass and an inherited class is called an "is a" relationship
    - A grasshopper "is a" insect
    - a poodle "is a" insect
    - a car "is a" vehicle
- A specialized object has:
    - All of the characteristics of the general object, plus
    - Additional character8istics that make it special.
- In object-oriented programming, inheritance is used to create an "is a" relationship among classes.

Overriding Methods
- We can override methods so that a subclass (derived) can act differently from its superclass (parent)

Accessing Superclass Members
- We can access shadowed methods of the superclass using the super() method

Looking up Attributes Names on Classes
- An attribute reference is resolved using a search procedure that checks
    - Instance's namespace
    - Class's namespace
    - Namespaces of base classes

"""

# Derived Classes
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

class SavingsAccount(Account):
    def __init__(self, balance, rate):
        Account.__init__(self, balance) # We can build on another class by deriving a new class to inherit it
        self.interest_rate = rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        Account.deposit(self, interest)

# Overriding Methods Example
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

class CheckingAccount(Account):
    transaction_fees = 3
    free_transactions = 4

    def __init__(self, balance):
        self.transaction_count = 0
        super().__init__(balance)

    def deposit(self, amount):
        self.transaction_count += 1
        Account.deposit(self, amount)

    def withdraw(self, amount):
        self.transaction_count += 1
        Account.withdraw(self, amount)

# Accessing Superclass Members Example
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount


class CheckingAccount(Account):
    transaction_fees = 3
    free_transactions = 4

    def __init__(self, balance):
        self.transaction_count = 0
        super().__init__(balance)

    def deposit(self, amount):
        self.transaction_count += 1
        super().deposit(amount)
        # Account.deposit(self, amount)
        # super().deposit(amount) is equivalent to Account.deposit(self.amount)

    def withdraw(self, amount):
        self.transaction_count += 1
        super().withdraw(amount)
        # Account.withdraw(self, amount)
        # super().withdraw(amount) is equivalent to Account.withdraw(self, amount)

# Knowledge Check
class Parent:
    def __init__(self, x, y=3):
        self.x = x
        self.y = y

class Child(Parent):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

c = Child(5, 7)
print(c.b, c.x, c.y) # print 7, 5, 3

# Looking up Attributes Names on Classes
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

class SavingsAccount(Account):
    def __init__(self, balance, rate):
        Account.__init__(self, balance) # We can build on another class by deriving a new class to inherit it
        self.interest_rate = rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        Account.deposit(self, interest)

class CheckingAccount(Account):
    transaction_fees = 3
    free_transactions = 4

    def __init__(self, balance):
        self.transaction_count = 0
        super().__init__(balance)

    def deposit(self, amount):
        self.transaction_count += 1
        super().deposit(amount)
        # Account.deposit(self, amount)
        # super().deposit(amount) is equivalent to Account.deposit(self.amount)

    def withdraw(self, amount):
        self.transaction_count += 1
        super().withdraw(amount)
        # Account.withdraw(self, amount)
        # super().withdraw(amount) is equivalent to Account.withdraw(self, amount)

sh = SavingsAccount(100, 0.02)
ch = CheckingAccount(300)

ch.deposit(20) # This is found in Checking account because it is defined there
sh.deposit(20) # found in Account because SavingsAccount does not define it there
