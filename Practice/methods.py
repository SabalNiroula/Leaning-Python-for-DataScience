class Bank:

    def __init__(self, name=""):
        self.name = name
        self.balance = 0
    
    def deposit(self, amount=0):
        self.balance+=amount
        print("{}, your amount after deposit is {}".format(self.name, self.balance))

    def withdraw(self, amount=0):
        if(self.balance>=amount):
            self.balance-=amount
            print("{}, your amount after withdrawal is {}".format(
                self.name, self.balance))
        else:
            print("{}, your balance is insufficient".format(self.name))


name = input("Enter your name: ")
bcc = Bank(name)

while(True):
    print("d-deposit, w-withdraw, e-exit")
    char = input("your choice : ")
    if(char == 'd'): 
        balance = int(input("Enter your balance: "))
        bcc.deposit(balance)
    elif(char == 'w'):
        balance = int(input("Enter your balance: "))
        bcc.withdraw(balance)
    else: break
