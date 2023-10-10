"""
Ian King's Calculator
The Goal of This Project: To develop a simple calculator application in Python that can perform basic arithmetic operations
These include: (+, -, *, /, //, %. **)
"""

# Function to perform addition
def add(num1, num2):
    return num1 + num2

# Function to perform subtraction
def subtract(num1, num2):
    return num1 - num2

# Function to perform multiplication
def multiply(num1, num2):
    return num1 * num2

# Function to perform division
def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Can't divide by zero"

# Function to perform floor division
def floor_divide(num1, num2):
    if num2 != 0:
        return num1 // num2
    else:
        return "Can't divide by zero"

# Function to perform modulus
def modulus(num1, num2):
    if num2 != 0:
        return num1 % num2
    else:
        return "Can't divide by zero"

# Function to perform power
def power(num1, num2):
    return num1 ** num2

# Now put all of those functions into one 'calculator' function
def calculator():
    # Get user input for numbers and operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /, //, %, **): ")
    
    # Perform each operation and return the result
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)
    elif operation == '//':
        return floor_divide(num1, num2)
    elif operation == '%':
        return modulus(num1, num2)
    elif operation == '**':
        return power(num1, num2)
    else:
        return "Please use a valid operation"

# Test cases for each operation 
def test_calculator():
    
    # Addition Test Case
    result = add(1, 2)
    assert result == 3, f"Expected 3, but got {result}"

    # Subtraction Test Case
    result = subtract(10, 6)
    assert result == 4, f"Expected 4, but got {result}"

    # Multiplication Test Case
    result = multiply(4, 5)
    assert result == 20, f"Expected 20, but got {result}"

    # Division Test Case
    result = divide(8, 2)
    assert result == 4, f"Expected 4, but got {result}"

    # Floor Division Test Case
    result = floor_divide(10, 3)
    assert result == 3, f"Expected 3, but got {result}"

    # Modulus Test Case
    result = modulus(9, 4)
    assert result == 1, f"Expected 1, but got {result}"

    # Power Test Case
    result = power(3, 2)
    assert result == 9, f"Expected 9, but got {result}"

    print("All tests passed")

# Run the test
test_calculator()

# Example
result = calculator()
print("Result:", result)

# First input was 2
# Second input was 3
# Third input was '+'
# Printed "Result: 5.0"