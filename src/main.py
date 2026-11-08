from decimal import Decimal, InvalidOperation
from getpass import getpass

from auth import create_user, login
from account import get_balance, deposit, withdraw, transfer, get_transactions
from account import get_account_id as find_account_id


def get_amount(message):

    while True:
        try:
            amount = Decimal(input(message))

            if not amount.is_finite():
                print("Please enter a valid number.")
                continue

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            if amount.as_tuple().exponent < -2:
                print("Please enter at most two decimal places.")
                continue

            return amount

        except InvalidOperation:
            print("Please enter a valid number.")


def get_account_id(message):

    while True:
        try:
            account_id = int(input(message))

            if account_id <= 0:
                print("Account ID must be greater than zero.")
                continue

            return account_id

        except ValueError:
            print("Please enter a valid account ID.")


def main():

    while True:
        print("\n================================")
        print("          SECUREBANK")
        print("1. Create account")
        print("2. Login")
        print("3. Exit")

        option = input("\nChoose an option: ")

        if option == "1":
            create_account_menu()

        elif option == "2":
            login_menu()

        elif option == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


def create_account_menu():

    print("\n========== CREATE ACCOUNT ==========")

    name = input("Name: ")
    email = input("Email: ")
    password = getpass("Password: ")

    result = create_user(name, email, password)

    print(result)


def login_menu():

    print("\n============== LOGIN ==============")

    email = input("Email: ")
    password = getpass("Password: ")

    user = login(email, password)

    if user:
        print(f"\nWelcome, {user['name']}!")

        account_id = find_account_id(user["id"])
        print(f"Your account ID: {account_id}")

        user_menu(user)
    else:
        print("Invalid email or password.")


def user_menu(user):

    while True:
        print("\n================================")
        print("          ACCOUNT MENU")
        print("================================")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Statement")
        print("6. Logout")

        option = input("\nChoose an option: ")

        if option == "1":
            balance = get_balance(user["id"])
            print(f"\nYour balance: R$ {balance:.2f}")

        elif option == "2":
            amount = get_amount("Amount to deposit: R$ ")

            result = deposit(user["id"], amount)

            print(result)

        elif option == "3":
            amount = get_amount("Amount to withdraw: R$ ")

            result = withdraw(user["id"], amount)

            print(result)

        elif option == "4":
            receiver_account_id = get_account_id("Receiver account ID: ")

            amount = get_amount("Amount to transfer: R$ ")

            result = transfer(user["id"], receiver_account_id, amount)

            print(result)

        elif option == "5":
            transactions = get_transactions(user["id"])

            print("\n========== STATEMENT ==========")

            if not transactions:
                print("No transactions found.")
            else:
                for transaction in transactions:
                    transaction_type = transaction[0]
                    amount = transaction[1]
                    created_at = transaction[2]
                    sender_name = transaction[3]
                    receiver_name = transaction[4]
                    sender_user_id = transaction[5]

                    if transaction_type == "DEPOSIT":
                        print(
                            f"DEPOSIT: + R$ {amount:.2f} | {created_at}"
                        )

                    elif transaction_type == "WITHDRAW":
                        print(
                            f"WITHDRAW: - R$ {amount:.2f} | {created_at}"
                        )

                    elif transaction_type == "TRANSFER":
                        if sender_user_id == user["id"]:
                            print(
                                f"TRANSFER TO {receiver_name}: "
                                f"- R$ {amount:.2f} | {created_at}"
                            )
                        else:
                            print(
                                f"TRANSFER FROM {sender_name}: "
                                f"+ R$ {amount:.2f} | {created_at}"
                            )

            print("===============================")

        elif option == "6":
            print("Logging out...")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()