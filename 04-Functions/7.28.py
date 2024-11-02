def f(dice):
    max_count = 1  # Maximum count of consecutive identical digits
    current_count = 1  # Current count of the same digit
    max_digit = dice[0]  # The digit that has the maximum consecutive count

    # Iterate through the dice results starting from the second character
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:  # If the current digit is the same as the previous one
            current_count += 1  # Increment the current count
        else:
            # Update max_count and max_digit if needed
            if current_count > max_count:
                max_count = current_count
                max_digit = dice[i - 1]  # Update the max_digit to the previous digit
            current_count = 1  # Reset current count for the new digit

    # Final check to update max_count and max_digit for the last sequence
    if current_count > max_count:
        max_digit = dice[-1]  # Update the max_digit to the last digit
        max_count = current_count

    return int(max_digit)  # Return the digit as an integer

# Test examples
print(f("5233165554211"))  # Output: 5
print(f("2133"))           # Output: 3