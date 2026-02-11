def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b

    def menu(self):
        print("\n========== CALCULATOR MENU ==========")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        print("====================================")

    def run(self):
        while True:
            self.menu()
            choice = input("Select an option (1-5): ")

            if choice == '5':
                print("Thank you for using the calculator. Goodbye!")
                break

            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice! Enter a number between 1 to 5.")
                continue

            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                result = self.add(num1, num2)
                print(f"{num1} + {num2} = {result}")

            elif choice == '2':
                result = self.subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")

            elif choice == '3':
                result = self.multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")

            elif choice == '4':
                result = self.divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

calc = Calculator()
calc.run()
