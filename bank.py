import random

class Customer:
    def __init__(self, name):
        self.name = name
        self.details = []

    def create_details(self):
        phone = int(input("Enter your phone number: "))
        password = input("Create Your Password: ")
        account_number = random.randint(1000, 9999)
        self.details = [phone, password, account_number, 0]
        print("Account Number:", account_number)

class Herapheri:
    def __init__(self, bank):
        self.bank = bank
    def transaction_menu(self, name):
        while True:
            print("\nTransaction Menu")
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Check balance")
            print("4. Transfer")
            print("5. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.lena(name)
            elif choice == "2":
                self.dena(name)
            elif choice == "3":
                self.paisa(name)
            elif choice == "4":
                self.idharudharkarna(name)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def lena(self, name):
            customer = self.bank.customers[name]
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                customer.details[3] += amount
                print(f"Amount ₹{amount:.2f} deposited successfully!")
            else:
                print("Invalid amount. Please enter a positive value.")

    def dena(self, name):
            customer = self.bank.customers[name]
            amount = float(input("Enter amount to withdraw: "))
            if amount > 0:
                if customer.details[3] >= amount:
                    customer.details[3] -= amount
                    print(f"Amount ₹{amount:.2f} withdrawn successfully!")
                else:
                    print("Insufficient balance.")
            else:
                print("Invalid amount. Please enter a positive value.")
    def paisa(self, name):
        customer = self.bank.customers[name]
        print("Your current balance is",customer.details[3])
    def idharudharkarna(self,name):
        customer = self.bank.customers[name]
        other=input("Enter reciver's name")
        if other in self.bank.customers:
            other_customer=self.bank.customers[other]
            amount = float(input("Enter amount to be transfered: "))
            password = input("Enter your password: ")
            if password==customer.details[1]:
                if customer.details[3] >= amount:
                    customer.details[3] -= amount
                    other_customer.details[3]+=amount
                    print("GAYA PAISA😭 ")
                else:
                    print("Insufficient balance.")
            else:
                    print("WORNG PASSWORD.")
        else:
                print("Recipient not found.")

class Bank:
    def __init__(self):
        self.customers = {}

    def create_account(self, name):
        if name in self.customers:
            print("Account already exists for", name)
        else:
            new_customer = Customer(name)
            new_customer.create_details()
            self.customers[name] = new_customer
            print(f"Account of '{name}' created successfully...")

    def remove_account(self, name):
        if name in self.customers:
            customer = self.customers[name]
            account_number = int(input("Enter your account number: "))
            password = input("Enter your password: ")
            if account_number == customer.details[2] and password == customer.details[1]:
                del self.customers[name]
                print(f"Account for '{name}' deleted successfully.")
            else:
                print("Invalid Account Number or Password.")
        else:
            print("Account not found for", name)

    def update_account(self, name):
        if name in self.customers:
            customer = self.customers[name]
            account_number = int(input("Enter your account number: "))
            password = input("Enter your current password: ")
            if account_number == customer.details[2] and password == customer.details[1]:
                update_choice = input("What would you like to update?\n"
                                      "1. Phone number\n"
                                      "2. Password\n"
                                      "Enter your choice: ")
                if update_choice == "1":
                    new_phone = int(input("Enter new phone number: "))
                    customer.details[0] = new_phone
                elif update_choice == "2":
                    new_password = input("Enter new password: ")
                    customer.details[1] = new_password
                else:
                    print("Invalid choice.")
                print("Account details updated successfully.")
            else:
                print("Invalid Account Number or Password.")
        else:
            print("Account not found for", name)

    def use_account(self, name):
        if name in self.customers:
            customer = self.customers[name]
            account_number = int(input("Enter your account number: "))
            password = input("Enter your password: ")
            if account_number == customer.details[2] and password == customer.details[1]:
                herapheri = Herapheri(self)
                herapheri.transaction_menu(name)
            else:
                print("Invalid uaser id or password")
        else:
            print("Account not found for", name)

    def main_menu(self):
        while True:
            print("\nWelcome to Ameero's Bank")
            print("1. Create Account")
            print("2. Use Account")
            print("3. Update Account")
            print("4. Delete Account")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter Account holder name: ")
                self.create_account(name)
            elif choice == "2":
                name = input("Enter Account holder name: ")
                self.use_account(name)
            elif choice == "3":
                name = input("Enter Account holder name: ")
                self.update_account(name)
            elif choice == "4":
                name = input("Enter Account holder name: ")
                self.remove_account(name)
            elif choice == "5":
                print("Goodbye!💦")
                break
            else:
                print("Invalid choice. Please try again.")

bank = Bank()
bank.main_menu()
