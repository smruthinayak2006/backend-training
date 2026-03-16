def get_numbers():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numbers only.")


def get_choice():
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ["1", "2", "3", "4"]:
            return choice
        print("Invalid choice. Select 1–4.")