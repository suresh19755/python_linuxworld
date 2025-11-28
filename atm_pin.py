bal = 5000
pin = 1234
tries = 0

print("--- Welcome to Python ATM ---")

while tries < 3:
    try:
        p = int(input("\nEnter PIN to access: "))

        if p == pin:
            print("Access Granted!")
            
            while True:
                print("\n1. Check Balance")
                print("2. Withdraw Cash")
                print("3. Deposit Cash")
                print("4. Exit")
                
                choice = input("Choose an option (1-4): ")

                if choice == '1':
                    print("Your total balance is:", bal)

                elif choice == '2':
                    amt = int(input("Enter amount to withdraw: "))
                    if amt > bal:
                        print("Failed: Insufficient funds.")
                    elif amt <= 0:
                        print("Enter a valid amount.")
                    else:
                        bal = bal - amt
                        print("Success! Withdrawn:", amt)
                        print("Remaining Balance:", bal)

                elif choice == '3':
                    d_amt = int(input("Enter amount to deposit: "))
                    if d_amt > 0:
                        bal = bal + d_amt
                        print("Deposit successful.")
                        print("New Balance:", bal)
                    else:
                        print("Cannot deposit 0 or negative money.")

                elif choice == '4':
                    print("Thank you for using our ATM. Bye!")
                    tries = 10  
                    break 
                
                else:
                    print("Invalid option selected.")

        else:
            tries = tries + 1
            left = 3 - tries
            print("Wrong PIN! You have", left, "attempts left.")
            
            if tries == 3:
                print("\nALERT: Card blocked due to multiple wrong attempts.")

    except ValueError:
        print("Error: Please enter numbers only.")