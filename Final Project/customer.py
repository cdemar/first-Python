#   Programmer: Cory DeMar
#   ComSc 20
#   Assognment #17
#   The Bank Account Class
#   5-22-17
#
#   Customer program.
#
#   This program constructs a dictionary of accounts keyed by account number
#   from a text file named accounts.dat. This file has one account per
#   line, with the account number, customer name, PIN, and balance,
#   separated by colons. For example, one entry might be:
#
#   10627:Georges Remi:0174:3571.85
#
#   The program then repeatedly allows customers to "log in" with account
#   number and PIN. (three tries). If user presses ENTER when asked for
#   account number, the program ends.
#
#   Once authenticated, the customer can deposit, withdraw, or finish.
#   When the customer finishes, the program writes the dictionary back to
#   the accounts.dat file in the same format as previously described.

import account

accounts = {}

def create_dictionary():
    """Create dictionary of accounts from a data file that has
    acct number, name, pin, and current balance separated by colon"""
    infile = open('accounts.dat', 'r')
    for line in infile:
        [number, name, pin, balance] = line.strip().split(':')
        acct = account.Account(number, name, pin, float(balance))
        accounts[number] = acct
    infile.close()

def write_accounts():
    """Write back the accounts.dat file after customer finishes transaction."""
    key_list = list(accounts.keys())
    key_list.sort()
    outfile = open('accounts.dat', 'w')
    for key in key_list:
        outfile.write(str(accounts[key]) + '\n')
    outfile.close()
    
def input_account_number():
    """Return an account number as a string"""
    result = input('Enter account number (or ENTER to quit): ')
    while result !='' and result not in accounts:
        print('Invalid account number.')
        result = input('Enter account number (or ENTER to quit): ')
    return result

def input_pin():
    """Return a 4-digit PIN as a string"""
    answer = input('Enter a 4-digit PIN: ')
    while not (answer.isnumeric() and len(answer) == 4):
        print('Your PIN must be all digits and exactly four digits long.')
        answer = input('Enter a 4-digit PIN: ')
    return answer

def login(account_number): 
    """Given an account number, give customer three tries to provide
    correct PIN. Return True if valid, False otherwise."""
    n_tries = 1
    account = accounts[account_number]
    pin = input_pin()
    while n_tries < 3 and pin != account.pin:
        n_tries += 1
        pin = input_pin()
    return pin == account.pin

def do_deposit(account):
    """Deposit to the given account (which is an object)."""
    amount = float(input("Enter amount to deposit: $"))
    while amount < 0:
        print('Amount cannot be negative.')
        amount = float(input('Enter amount to deposit: $'))
    account.deposit(amount)
    
def do_withdrawal(account):
    """Withdraw from the given account (which is an object)."""
    amount = float(input('Enter amount to withdeaw: $'))
    while amount < 0 or amount > account.balance:
        print('Amount cannot be negative or greater than balance.')
        amount = float(input('Enter amount to withdeaw: $'))
    account.withdraw(amount)
        
def do_transactions(account):
    """Ask to Deposit, Withdraw, or Finish; write new account file
    when finished. The account parameter is an Account object."""
    action = input('D)eposit, W)ithdraw, or F)inish: ')
    action = action.upper()
    
    while action != 'F':
        if action == 'D':
            do_deposit(account)
            print('Your balance is now ',show_balance(account))
        elif action == 'W':
            do_withdrawal(account)
            print('Your balance is now ', show_balance(account))
        action = input('D)eposit, W)ithdraw, or F)inish: ')
        action = action.upper()

    write_accounts()
    print('Thank you for banking with us', account.name)
    print()

def show_balance(account):
    """Return a string giving current account balance in proper
    format (2 decimals and dollar sign)"""
    return '$' + format(account.balance, '.2f')

def main():
    create_dictionary()
    account_number = input_account_number()
    while account_number != '':
        if login(account_number):
            account = accounts.get(account_number)
            print('Welcome, ', account.name, '! Your current balance is ',
                  show_balance(account), '.', sep='')
            do_transactions(account)
        else:
            print('Sorry, could not validate you as a customer.')

        account_number = input_account_number()

main()

    
