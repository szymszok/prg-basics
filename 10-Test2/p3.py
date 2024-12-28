def f(array2D):
    """Returns True if the sum of each row equals the sum of the corresponding column."""
    n = len(array2D)  # Assuming the array is n x n
    
    for i in range(n):
        row_sum = sum(array2D[i])  # Sum of the i-th row
        col_sum = sum(array2D[j][i] for j in range(n))  # Sum of the i-th column
        
        if row_sum != col_sum:
            return False
            
    return True

# Example usage:
result1 = f([
    [3, 7, 2], 
    [4, 2, 5], 
    [5, 2, 1]]
    )
print(result1)  # Output: True

result2 = f([[3, 7, 2], [4, 2, 5], [9, 2, 1]])
print(result2)  # Output: False
