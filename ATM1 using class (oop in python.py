class bankaccount:

    def __init__(self):
        self.balance = 0

    def withdraw(self,amount):
        self.balance -= amount
        print('Your Remaining Balance is',self.balance)

    def deposit(self,amount):
        self.balance +=amount
        return self.balance

a = bankaccount()
b = bankaccount()

a.deposit(int(input('enter amount you want to deposit')))

a.withdraw(int(input('enter the amount you want to withdraw')))
