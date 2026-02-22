def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero"

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == "1":
        print("Result:", add(num1, num2))

    elif choice == "2":
        print("Result:", subtract(num1, num2))

    elif choice == "3":
        print("Result:", multiply(num1, num2))

    elif choice == "4":
        if num2 != 0:
            print("Result:", divide(num1, num2))
        else:
            print("Error: Cannot divide by zero")

    else:
        print("Invalid choice")

    again = input("Do you want to calculate again? (yes/no): ")

    if again.lower() != "yes":
        print("Goodbye!")
        break