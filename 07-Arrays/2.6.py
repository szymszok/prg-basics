# Initial square matrix
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Get the size of the matrix (assuming it's a square matrix)


# Replace the values of the main diagonal with 1
for i in range(len(matrix)):
    matrix[i][i] = 1  # Set the diagonal element to 1

# Print the modified array
for row in matrix:
    print(' '.join(map(str, row)))  # Print each row with space-separated values