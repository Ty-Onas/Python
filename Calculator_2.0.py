import math

# Calculator class
class Calculator:
    def __init__(self):
        # Dictionary to store available operations
        self.operations = {'+': self.add, '-': self.subtract, '*': self.multiply, '/': self.divide}

    def add_operation(self, symbol, func):
        """Add a new operation to the calculator."""
        self.operations[symbol] = func

    def calculate(self, num1, symbol, num2):
        """Perform the calculation based on the provided symbol."""
        # Error handling for invalid inputs
        if symbol not in self.operations:
            raise ValueError(f"Invalid operation '{symbol}'")
        if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
            raise ValueError("Inputs must be numbers")

        # Retrieve and perform the operation
        operation_func = self.operations[symbol]
        return operation_func(num1, num2)

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2

# Create functions for advanced mathematical operations
def exponentiate(num1, num2):
    return num1 ** num2

def square_root(num1, num2=None):
    if num1 < 0:
        raise ValueError("Cannot calculate the square root of a negative number")
    return math.sqrt(num1)

def logarithm(num1, num2=None):
    if num1 <= 0:
        raise ValueError("Logarithm base must be greater than zero")
    return math.log(num1)

# Main program
def main():
    # Create a Calculator object
    calc = Calculator()

    # Adding advanced mathematical operations
    calc.add_operation('^', exponentiate)  # Exponentiation
    calc.add_operation('sqrt', square_root)  # Square root
    calc.add_operation('log', logarithm)  # Logarithm

    while True:
        # User input for the first number, operation symbol, and second number
        try:
            num1 = float(input("Enter the first number: "))
            symbol = input("Enter operation (+, -, *, /, ^, sqrt, log): ")
            
            # For square root or log, only num1 is used
            if symbol in ['sqrt', 'log']:
                num2 = None
            else:
                num2 = float(input("Enter the second number: "))

            # Perform the calculation
            result = calc.calculate(num1, symbol, num2)
            print(f"Result: {result}")
        
        except Exception as e:
            print(f"Error: {e}")

        # Check if the user wants to perform another calculation
        continue_calculating = input("Do you want to continue? (yes/no): ").lower()
        if continue_calculating != 'yes':
            break

# Run the main program
if __name__ == "__main__":
    main()

print("Thank you for using Calculator 2.0!")