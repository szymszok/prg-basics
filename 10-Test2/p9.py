import csv

def f(value):
    """Returns the number of employees with a salary greater than or equal to the given value."""
    count = 0
    
    # Open the CSV file
    with open('data.csv', mode='r') as file:
        reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
        for row in reader:
            # Convert salary from string to float (or int)
            salary = float(row['salary'])
            # Check if the salary is greater than or equal to the given value
            if salary >= value:
                count += 1
    
    return count

# Example usage:
result = f(60000)
print(result)  # This will print the number of employees with a salary >= 60000