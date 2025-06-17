while True:
    try:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        c=input("Enter a operator (+, -, *, /): ")
        if "+" in c:
            print(f"{a} + {b} = {a+b}")
        elif "-" in c:
            print(f"{a} - {b} = {a-b}")
        elif "*" in c:
            print(f"{a} * {b} = {a*b}")
        elif "/" in c:
            print(f"{a} / {b} = {a/b}")
        else:
            print("Invalid operator")    
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")
    else:
        print("Calculation completed successfully.")
        break
    finally:
        print("Thank you for using the calculator.")    