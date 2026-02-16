import datetime

class account:
    def __init__(self, acc_number, name, initial_balance=0):
        self.acc_number = acc_number
        self.name = name
        self.balance = initial_balance
        self.history = []
        self._log("Account Created", initial_balance)

    def _log(self, trans_type, amount):
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.history.append({
            "timestamp": timestamp,
            "type": trans_type,
            "amount": amount,
            "balance_after": self.balance
        })

    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be greater than 0")
            return False
        
        self.balance += amount
        self._log("Deposit", amount)
        print(f"{self.name} deposited ${amount}. New Balance: ${self.balance}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than 0")
            return False
        if amount > self.balance:
            print("Error: Insufficient Balance")
            return False
        
        self.balance -= amount
        self._log("Withdrawal", amount)
        print(f"{self.name} withdrew ${amount}. New Balance: ${self.balance}")
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, target_account):
        print(f"{self.name} initiating transfer of ${amount} to {target_account.name}...")
        if self.withdraw(amount):
            target_account.deposit(amount)
            self.history[-1]['type'] = f"Transfer Out to {target_account.acc_number}"
            target_account.history[-1]['type'] = f"Transfer In from {self.acc_number}"
            print("Transfer successful.")
            return True
        print("Transfer failed.")
        return False

    def __str__(self):
        return (f"Account: {self.acc_number} | Holder: {self.name} | "
                f"Balance: ${self.balance}")


if __name__ == "__main__":
    
    acc1 = account("A001", "Alex", 0)
    acc2 = account("A002", "Nihal", 0)
    acc3 = account("A003", "Omkar", 0)
    acc4 = account("A004", "Jason", 0)
    
    acc1.deposit(500)
    acc2.deposit(0)
    acc3.deposit(-1)
    acc4.deposit(500)
    
    acc1.withdraw(200)
    acc2.withdraw(200)
    acc3.withdraw(200)
    acc4.withdraw(200)
    
    acc1.transfer(300, acc3)
    acc3.transfer(300, acc2)
    acc2.transfer(1000, acc3)
    acc4.transfer(0, acc3)

    print("\n" + str(acc1))
    print("Transaction History")
    for record in acc1.history:
        print(record)
        
    print("\n" + str(acc2))
    print("Transaction History")
    for record in acc2.history:
        print(record)
    
    print("\n" + str(acc3))
    print("Transaction History")
    for record in acc3.history:
        print(record)
    
    print("\n" + str(acc4))
    print("Transaction History")
    for record in acc4.history:
        print(record)

