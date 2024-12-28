def f(subjects):
    """Returns the name of the subject with the highest average grade."""
    highest_average = 0  # Initialize to negative infinity
    subject_with_highest_average = ' '
    
    for subject, grades in subjects.items():
        average = sum(grades) / len(grades)  # Calculate the average grade
        
        if average > highest_average:
            highest_average = average
            subject_with_highest_average = subject
            
    return subject_with_highest_average

# Example usage:
result = f({"math": [3, 4, 4], "geo": [5, 4, 4, 4], "comp": [5, 4]})
print(result)  # Output: "comp"