class User:
    def __init__(self, user_name,password, initial_deposit=0):
        self.name = user_name
        self.password=password
        
        self.balance = initial_deposit
        self.loan_amount = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
        else:
            print("Insufficient funds")

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.deposit(amount)
            self.transaction_history.append(f"Transferred: {amount} to {recipient.name}")
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.balance

    def take_loan(self):
        if self.loan_amount == 0:
            self.loan_amount = self.balance * 2
            self.balance += self.loan_amount
            self.transaction_history.append(f"Took a loan: {self.loan_amount}")
        else:
            print("You have already taken a loan")

    def view_transaction_history(self):
        return self.transaction_history


class Admin:
    def __init__(self):
        self.users = []

    def create_account(self, user_name, password):
        new_user = User(user_name,password)
        self.users.append(new_user)
        return new_user

    def total_balance(self):
        total = sum(user.balance for user in self.users)
        return total

    def total_loan_amount(self):
        total = sum(user.loan_amount for user in self.users)
        return total

    def toggle_loan_feature(self, enable):
        User.take_loan = User.take_loan if enable else lambda self: print("Loan feature is disabled")


if __name__ == "__main__":
    admin = Admin()
    user=User('bob',78787,900)



    user1 = admin.create_account("John", 1001)
    user2 = admin.create_account("Alice", 1002)

    user1.deposit(200)
    user1.withdraw(100)
    user1.transfer(user2, 150)
    user1.take_loan()

    print('Total balance of user1:',user.check_balance())

    print("Total balance in the bank:", admin.total_balance())
    print("Total loan amount in the bank:", admin.total_loan_amount())


    admin.toggle_loan_feature(enable=False)
    user1.take_loan()  
