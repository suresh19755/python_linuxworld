print("--- CINEMA HALL ENTRY ---")
print("Movie: BAHUBALI : THE Beginning (Rated R)")
print("-----------------------------------")

while True:
    try:
        my_age = int(input("\nAge: "))
        having_pass = input("Have ticket? (y/n): ").lower()

        if my_age >= 18:
            if having_pass == 'y':
                print("Welcome inside.")
            else:
                print("Please buy ticket.")

        elif my_age >= 13:
            if having_pass == 'y':
                print("Entry allowed (Check ID).")
            else:
                print("Ticket required.")
            
        else:
            print("Too young for this movie.")
            mom_dad = input("Is parent with you? (y/n): ").lower()
        
            if mom_dad == 'y':
                if having_pass == 'y':
                    print("Allowed with parent.")
                else:
                    print("Buy ticket first.")
            else:
                print("Sorry, not allowed.")

    except:
        print("Error: Input number only")