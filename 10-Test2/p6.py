import json

def f(years, course, average_grade):
    """Returns the number of students who have at least 'years' of study 
    and an average grade of at least 'average_grade' in the given 'course'."""
    
    count = 0
    
    # Read the JSON file
    with open('students.json', 'r') as file:
        students = json.load(file)  # Load the JSON data
        
        for student in students:
            # Check if the student has at least the required years
            if student['years'] >= years:
                # Check if the student has the specified course
                if course in student['courses']:
                    # Calculate the average grade for the specified course
                    grades = student['courses'][course]
                    average = sum(grades) / len(grades)
                    
                    # Check if the average grade meets the requirement
                    if average >= average_grade:
                        count += 1
    
    return count

# Example usage:
result = f(21, "statistics", 4)
print(result)  # This will print the number of students meeting the criteria.