from Backend.calculator.operations import add, subtract, multiply, divide
from utils import get_numbers, get_choice

history = []

while True:

    num1, num2 = get_numbers()

    print("1 Add")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")

    choice = get_choice()

    if choice == "1":
        result = add(num1, num2)
        history.append(f"{num1} + {num2} = {result}")

    elif choice == "2":
        result = subtract(num1, num2)
        history.append(f"{num1} - {num2} = {result}")

    elif choice == "3":
        result = multiply(num1, num2)
        history.append(f"{num1} * {num2} = {result}")

    elif choice == "4":
        try:
            result = divide(num1, num2)
        except ValueError as e:
            print(e)
            continue

        history.append(f"{num1} / {num2} = {result}")

    print("Result:", result)

    again = input("Again? (yes/no): ").lower()
    if again != "yes":
        print("\nHistory:")
        for h in history:
            print(h)
        break