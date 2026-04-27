from pydantic import validate_call
class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    @validate_call
    def deposit(self, amount:float):
        if amount < 0:
            print("Invalid deposit")
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance = self.balance - amount

    def transfer(self, other_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
        print(f"Transferred {amount}")

    def __str__(self):
        return f"{self.owner}: {self.balance}"


def process_transactions(account, transactions):
    for i in range(len(transactions)):
        t = transactions[i]

        if t["type"] == "deposit":
            account.deposit(t["amount"])

        elif t["type"] == "withdraw":
            account.withdraw(t["amount"])

        elif t["type"] == "transfer":
            account.transfer(t["to"], t["amount"])

    return account.balance


# Setup
acc1 = BankAccount("Alice", 100)
acc2 = BankAccount("Bob", 50)

transactions = [
    {"type": "deposit", "amount": 50},
    {"type": "withdraw", "amount": 200},
    {"type": "transfer", "amount": 30, "to": acc2},
    {"type": "deposit", "amount": -20},
]

final_balance = process_transactions(acc1, transactions)

print(acc1)
print(acc2)
print("Final balance:", final_balance)

# Add this line to keep the program running
input("Press Enter to exit...")
