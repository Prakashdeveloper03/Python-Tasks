class ATM:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Successful")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Withdrawal Failed, Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal Successful")

    def check_balance(self):
        print(f"Your balance is {self.balance}")


def main():
    account = ATM()
    while True:
        print("\nATM Management System")
        print("--------------------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            amount = int(input("Enter deposit amount : "))
            account.deposit(amount)
        elif choice == "2":
            amount = int(input("Enter withdrawal amount : "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a number from 1-4.")
    print("Thank you for using the ATM Management System.")


if __name__ == "__main__":
    main()
