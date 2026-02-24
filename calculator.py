def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero"
    
history = []

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
        result = add(num1, num2)
        print("Result:", result)
        history.append(f"{num1} + {num2} = {result}")

    elif choice == "2":
        result = subtract(num1, num2)
        print("Result:", result)
        history.append(f"{num1} - {num2} = {result}")

    elif choice == "3":
        result = multiply(num1, num2)
        print("Result:", result)
        history.append(f"{num1} * {num2} = {result}")

    elif choice == "4":
        result = divide(num1, num2)
        print("Result:", result)
        history.append(f"{num1} / {num2} = {result}")

    else:
        print("Invalid choice")

    again = input("Do you want to calculate again? (yes/no): ")

    if again.lower() != "yes":
        print("\nCalculation History:")
        for item in history:
            print(item)

        print("Goodbye!")
        break