# Simple ATM System

accounts = {}   # stores account number and its details

while True:
    print("\n===== SIMPLE ATM SYSTEM =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # -------------------------------------
    # Create Account
    # -------------------------------------
    if choice == "1":
        name = input("Enter your name: ")
        acc_no = input("Create account number: ")
        pin = input("Create 4-digit PIN: ")

        if len(pin) != 4:
            print("PIN must be 4 digits!")
            continue

        accounts[acc_no] = {
            "name": name,
            "pin": pin,
            "balance": 0,
            "history": []
        }

        print("Account created successfully!")

    # -------------------------------------
    # Login
    # -------------------------------------
    elif choice == "2":
        acc_no = input("Enter account number: ")
        pin = input("Enter PIN: ")

        if acc_no not in accounts:
            print("Account does not exist!")
            continue

        if accounts[acc_no]["pin"] != pin:
            print("Incorrect PIN!")
            continue

        print(f"Welcome {accounts[acc_no]['name']}!")

        # User Menu
        while True:
            print("\n--- ATM MENU ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Mini Statement")
            print("5. Logout")

            opt = input("Enter option: ")

            # Deposit
            if opt == "1":
                amount = int(input("Enter amount: "))
                accounts[acc_no]["balance"] += amount
                accounts[acc_no]["history"].append(f"Deposited {amount}")
                print("Amount deposited!")

            # Withdraw
            elif opt == "2":
                amount = int(input("Enter amount: "))
                if amount > accounts[acc_no]["balance"]:
                    print("Insufficient balance!")
                else:
                    accounts[acc_no]["balance"] -= amount
                    accounts[acc_no]["history"].append(f"Withdrawn {amount}")
                    print("Amount withdrawn!")

            # Check Balance
            elif opt == "3":
                print("Balance:", accounts[acc_no]["balance"])

            # Mini Statement
            elif opt == "4":
                print("Last Transactions:")
                for h in accounts[acc_no]["history"][-5:]:
                    print("-", h)

            # Logout
            elif opt == "5":
                print("Logged out!")
                break

            else:
                print("Invalid option!")

    # -------------------------------------2
    
    # Exit
    # -------------------------------------
    elif choice == "3":
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice!")