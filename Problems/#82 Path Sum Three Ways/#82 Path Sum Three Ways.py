'''
Question Id: 82
Question Name: Path Sum: Three Ways

Find the minimal path sum from the left column to the right 
column in matrix.txt (right click and "Save Link/Target As..."), a 31K text 
file containing an 80 by 80 matrix. 
'''

from timeit import default_timer as timer #i want to see how much time the solution takes.

result = 0
start = timer()

from timeit import default_timer as timer

start = timer()

def min_path_sum(filename):
    # Obviously we need to read the matrix from the file
    with open(filename, 'r') as f:
        matrix = [[int(x) for x in line.split(',')] for line in f]

    #to get the number of rows and columns, so we can initialize the dp array
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize a dp array that will store the minimum path sums for each cell
    # we will update this array as we process the matrix, making sure to account min pahts from left to right, 
    # top to bottom and bottom to top. 
    dp = [[float('inf')] * cols for _ in range(rows)]
    # resulting dp matrix is a 2D array with the same dimensions as the input matrix,
    # where each cell (i, j) will contain the minimum path sum from the leftmost column to the cell (i, j).

    # Initialize the first column (starting points)
    for i in range(rows):
        dp[i][0] = matrix[i][0]
    #they are the same as the first column of the matrix, since we cant get less than that. :D

    # Process each column from left to right
    for j in range(1, cols):
        # First, carry over the previous column values (moving right)
        # the naive way to move right is to just add the value of the cell to the left of the current cell.
        for i in range(rows):
            dp[i][j] = dp[i][j-1] + matrix[i][j]

        # Then process top-to-bottom to allow downward movement
        # so we take account of the minimum path sum from the cell above the current cell
        for i in range(1, rows):
            dp[i][j] = min(dp[i][j], dp[i-1][j] + matrix[i][j])

        # Finally, process bottom-to-top to allow upward movement
        # so we take account of the minimum path sum from the cell below the current cell
        for i in range(rows-2, -1, -1):
            dp[i][j] = min(dp[i][j], dp[i+1][j] + matrix[i][j])

    # The minimum path sum will be the minimum value in the last column
    return min(dp[i][-1] for i in range(rows))

result = min_path_sum('0082_matrix.txt')

end = timer()

print(f"Result: {int(result)}")
print(f"Time taken: {end - start} seconds")

#the answer is : 260324 
#time it took : 0.01997631399990496 seconds