import math

while True:
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. divide")
    print("5. Power")
    print("6. Root")
    print("7. Quit")

    a = input("Choice: ")

    if a == '7':
        print("Bye!")
        break

    if a not in ('1', '2', '3', '4', '5', '6'):
        print("Invalid option.")
        continue

    try:
        if a == '6':
            val = float(input("Enter number: "))
            if val < 0:
                print("Can't do negative roots.")
            else:
                print("Answer:", math.sqrt(val))
        
        else:
            x = float(input("First num: "))
            y = float(input("Second num: "))

            if a == '1':
                print(f"Sum: {x + y}")
            elif a == '2':
                print(f"Diff: {x - y}")
            elif a == '3':
                print(f"Product: {x * y}")
            elif a == '4':
                if y != 0:
                    print(f"divide: {x/y}")
                else:
                    print("can't divide by zero")
            elif a == '5':
                print(f"Result: {math.pow(x, y)}")

    except ValueError:
        print("Numbers only please.")