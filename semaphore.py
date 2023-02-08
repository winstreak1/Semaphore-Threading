from threading import *
import time

# creating thread instance where count = 3
obj = Semaphore(3)

class BankAccount():

    def __init__(self, initial_money=0, owner='Anonymous'):
        self.money = initial_money
        self.owner = owner
        # We will keep each write access to money in an history file
        # In order to understand what Python does with your money
        self.history_file = open('/tmp/%s' % (owner,), 'w')

    def execute_deposit(self, amount, by='A customer'):
        self.history_file.write(
            'Customer %s is adding %s to bank account of %s containing %s\n' % (by, amount, self.owner, self.money))

        for ind in range(0, amount):
            self.money += 1
            time.sleep(1)

        self.history_file.write('Account money after %s deposit: %s\n' % (by, self.money))

    def execute_withdrawal(self, amount, by='B customer'):
        self.history_file.write(
            'Customer %s is withdrawing %s to bank account of %s containing %s\n' % (by, amount, self.owner, self.money))

        for ind in range(0, amount):
            self.money -= 1
            time.sleep(1)

        self.history_file.write('Account money after %s deposit: %s\n' % (by, self.money))

    def __del__(self):
        self.history_file.close()


class BankAccount():
    def __init__(self, initial_money=0, owner='Anonymous'):
        self.money = initial_money
        self.owner = owner
        # We will keep each write access to money in an history file
        # In order to understand what Python does with your money
        self.history_file = open('/tmp/%s' % (owner,), 'w')

    def execute_deposit(self, amount, by='A customer'):
        self.history_file.write(
            'Customer %s is adding %s to bank account of %s containing %s\n' % (by, amount, self.owner, self.money))
        self.money += amount
        self.history_file.write('Account money after %s deposit: %s\n' % (by, self.money))

    def execute_withdrawal(self, amount, by='A customer'):
        self.history_file.write(
            'Customer %s is adding %s to bank account of %s containing %s\n' % (by, amount, self.owner, self.money))
        self.money -= amount
        self.history_file.write('Account money after %s withdrawal: %s\n' % (by, self.money))
    def __del__(self):
        self.history_file.close()

my_account = BankAccount(1000, "WorldCompanyBigBoss")
t1 = Thread(target = my_account.execute_deposit, args =(100, "First customer: Thread-1"))
t2 = Thread(target = my_account.execute_deposit, args = (7500, "Second customer: Thread-2"))
t3 = Thread(target = my_account.execute_withdrawal, args = (200, "Second customer: Thread-3"))
t4 = Thread(target = my_account.execute_withdrawal, args = (50, "First customer: Thread-4"))

t1.start()
t2.start()
t3.start()
t4.start()