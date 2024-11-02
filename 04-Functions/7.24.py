def f(expression):
    # Initialize the result and the current number
    result = 0
    current_number = 0
    current_operator = '+'  # Start with a '+' operator

    # Remove spaces from the expression for easier processing
    expression = expression.replace(" ", "")

    for char in expression:
        if char.isdigit():  # If the character is a digit
            current_number = int(char)  # Convert it to an integer
        else:
            # If we encounter an operator, we apply the previous operator
            if current_operator == '+':
                result += current_number
            elif current_operator == '-':
                result -= current_number
            
            # Update the current operator
            current_operator = char

    # Apply the last number in the expression
    if current_operator == '+':
        result += current_number
    elif current_operator == '-':
        result -= current_number

    return result

# Przykład użycia:
print(f("2+3"))  
print(f("2+3-4+5-0"))  
