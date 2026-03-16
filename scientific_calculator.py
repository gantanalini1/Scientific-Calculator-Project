import math

history = []

while True:

    print("\n" + "="*40)
    print("        ULTIMATE SCIENTIFIC CALCULATOR")
    print("="*40)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Square Root")
    print("7. Power")
    print("8. Log")
    print("9. Sin")
    print("10. Cos")
    print("11. Tan")
    print("12. Factorial")
    print("13. Show History")
    print("14. Exit")
    print("="*40)

    choice = input("Enter your choice: ")

    try:

        if choice == '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = round(a + b, 2)
            print("Result:", result)
            history.append(f"{a} + {b} = {result}")

        elif choice == '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = round(a - b, 2)
            print("Result:", result)
            history.append(f"{a} - {b} = {result}")

        elif choice == '3':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = round(a * b, 2)
            print("Result:", result)
            history.append(f"{a} * {b} = {result}")

        elif choice == '4':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if b == 0:
                print("Error: Cannot divide by zero")
            else:
                result = round(a / b, 2)
                print("Result:", result)
                history.append(f"{a} / {b} = {result}")

        elif choice == '5':
            num = float(input("Enter number: "))
            result = round(num ** 2, 2)
            print("Result:", result)
            history.append(f"{num}² = {result}")

        elif choice == '6':
            num = float(input("Enter number: "))
            if num < 0:
                print("Error: Square root of negative number is not possible")
            else:
                result = round(math.sqrt(num), 2)
                print("Result:", result)
                history.append(f"√{num} = {result}")

        elif choice == '7':
            a = float(input("Enter base: "))
            b = float(input("Enter power: "))
            result = round(math.pow(a, b), 2)
            print("Result:", result)
            history.append(f"{a}^{b} = {result}")

        elif choice == '8':
            num = float(input("Enter number: "))
            if num <= 0:
                print("Error: Log undefined for zero or negative numbers")
            else:
                result = round(math.log(num), 2)
                print("Result:", result)
                history.append(f"log({num}) = {result}")

        elif choice == '9':
            num = float(input("Enter angle (radians): "))
            result = round(math.sin(num), 2)
            print("Result:", result)
            history.append(f"sin({num}) = {result}")

        elif choice == '10':
            num = float(input("Enter angle (radians): "))
            result = round(math.cos(num), 2)
            print("Result:", result)
            history.append(f"cos({num}) = {result}")

        elif choice == '11':
            num = float(input("Enter angle (radians): "))
            result = round(math.tan(num), 2)
            print("Result:", result)
            history.append(f"tan({num}) = {result}")

        elif choice == '12':
            num = int(input("Enter number: "))
            if num < 0:
                print("Error: Factorial not possible for negative numbers")
            else:
                result = math.factorial(num)
                print("Result:", result)
                history.append(f"{num}! = {result}")

        elif choice == '13':
            print("\n===== Calculation History =====")
            for item in history:
                print(item)

        elif choice == '14':
            print("Calculator closed.")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Error: Please enter valid numbers")