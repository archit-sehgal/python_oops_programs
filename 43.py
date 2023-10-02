class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    def deposit(self):
        self.depositAmount = int(input("enter amount to deposit: "))
        self.balance += self.depositAmount
        print(
            f"Amount of Rs {self.depositAmount} credited to accountNumber: {self.accountNumber}\nBalance amount is: {self.balance}"
        )
        print("---------------------------")
    def withdrawl(self):
        self.withdrawAmount=int(input("Enter Amount to withdraw: "))
        self.balance-=self.withdrawAmount
        print(
            f"Amount of Rs {self.withdrawAmount} debited from accountNumber: {self.accountNumber}\nBalance amount is: {self.balance}"
        )
        print("---------------------------")
    def bankFees(self):
        self.bankfeesAmount=(self.balance)*5/100
        print(f"Bank fees of 5% levied on your AccountNumber {self.accountNumber} is Rs: {self.bankfeesAmount}")
        print("---------------------------")
    def display(self):
        print("---------------------------")
        print(
            f"Person Name: {self.name}\nAccount Number: {self.accountNumber}\nBalance Amount: {self.balance}"
            )
        print("---------------------------")

call=BankAccount("12345678","Archit",10000)
call.withdrawl()
call.deposit()
call.bankFees()
askfordisplay=input("Show Account Details? Y/N: ").lower()
if askfordisplay=="y":
    call.display()
