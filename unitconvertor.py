def length_conv():
    print("\n--- Lengths ---")
    print("1. Meter -> KM")
    print("2. KM -> Meter")
    print("3. Meter -> CM")
    print("4. Foot -> Meter")
    print("5. Inch -> CM")

    try:
        op = int(input("Select: "))
        n = float(input("Enter Value: "))

        if op == 1:
            print(f"Ans: {n / 1000} km")
        elif op == 2:
            print(f"Ans: {n * 1000} m")
        elif op == 3:
            print(f"Ans: {n * 100} cm")
        elif op == 4:
            print(f"Ans: {n * 0.3048} m")
        elif op == 5:
            print(f"Ans: {n * 2.54} cm")
        else:
            print("Invalid selection")
    except ValueError:
        print("Invalid input")

def mass_conv():
    print("\n--- Mass ---")
    print("1. Kg -> Gram")
    print("2. Gram -> Kg")
    print("3. Kg -> Pound")
    print("4. Pound -> Kg")
    print("5. Ounce -> Gram")

    try:
        op = int(input("Choice: "))
        val = float(input("Weight: "))

        if op == 1:
            print("Result:", val * 1000, "g")
        elif op == 2:
            print("Result:", val / 1000, "kg")
        elif op == 3:
            print("Result:", val * 2.20462, "lbs")
        elif op == 4:
            print("Result:", val / 2.20462, "kg")
        elif op == 5:
            print("Result:", val * 28.3495, "g")
    except:
        print("Something went wrong.")

def temp_conv():
    print("\n--- Temperature ---")
    print("1. C -> F")
    print("2. F -> C")
    print("3. C -> K")
  
    try:
        ch = int(input("Op: "))
        deg = float(input("Temp: "))

        if ch == 1:
            print("Result:", (deg * 9/5) + 32, "F")
        elif ch == 2:
            print("Result:", (deg - 32) * 5/9, "C")
        elif ch == 3:
            print("Result:", deg + 273.15, "K")
        else:
            print("Not valid")
    except ValueError:
        print("Numbers only please")

def currency_conv():
    print("\n--- Currency (Approx) ---")
    print("1. INR -> USD")
    print("2. USD -> INR")
   
    usd_rate = 83.0

    try:
        c = int(input("Select: "))
        money = float(input("Amount: "))

        if c == 1:
            print(f"{money} INR is {money / usd_rate} USD")
        elif c == 2:
            print(f"{money} USD is {money * usd_rate} INR")
        else:
            print("Coming soon...")
    except ValueError:
        print("Enter digits only.")

while True:
    print("\n=== CONVERTER APP ===")
    print("1. Length")
    print("2. Mass")
    print("3. Temperature")
    print("4. Currency")
    print("5. Quit")

    try:
        main_opt = input("Pick category: ")
        
        if main_opt == '1':
            length_conv()
        elif main_opt == '2':
            mass_conv()
        elif main_opt == '3':
            temp_conv()
        elif main_opt == '4':
            currency_conv()
        elif main_opt == '5':
            print("Exiting... Bye!")
            break
        else:
            print("Try 1-5")
            
    except Exception as e:
        print("Error:", e)