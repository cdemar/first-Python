#   Programmer: Cory DeMar
#   ComSc 20
#   Assognment #17
#   The Bank Account Class
#   5-22-17
#
#   Account class.
#   Each account has an account number (acct_number), account holder's name,
#   PIN (4 character string) and current balance.

class Account:

    def __init__(self, acct_number, name, pin, balance):
        """Intialize corresponding members of the Account object
        being created."""
        self.acct_number = acct_number
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        """Return a string that has the account number, account holder's
        name, PIN, and balance; separated by colons."""
        return format(self.acct_number) + ':' + format(self.name) + ':' + format(self.pin) + ':' + format(self.balance)

    def deposit(self, amount):
        """Add the amount to the balance if the amount is greater than
        or equal to zero. If not, leave the object untouched."""
        if amount >= 0:
            self.balance += amount

    def withdraw(self, amount):
        """Subtract the amount from the balance if the amount is greater than
        or equal to zero and less than or equal to the current balance. If
        not, leave the object untouched."""
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
