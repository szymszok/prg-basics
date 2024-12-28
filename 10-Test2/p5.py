def f(first_letter, last_letter):
    """Returns the number of words that start with first_letter and end with last_letter."""
    count = 0
    
    # Open the file and read its contents
    with open('data.txt', 'r') as file:
        # Read all lines from the file
        for line in file:
            # Split the line into words
            words = line.split()
            # Check each word
            for word in words:
                # Check if the word starts with first_letter and ends with last_letter
                if word.startswith(first_letter) and word.endswith(last_letter):
                    count += 1
                    
    return count

# Example usage:
# result = f('a', 'e')
# print(result)  # This would print the count of words starting with 'a' and ending with 'e'.