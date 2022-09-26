# matrix = [[1, 2, 3], [4, 5, 6]]

row =  int (input("Enter number of rows     : "))
col =  int (input("Enter number of columns  : "))

matrix=[]
print("\nEnter values in row")

# TODO take input in matrix
for i in range(row):
    m = []
    for j in range(col):
        m.append(int(input("Enter your element : ")))
    matrix.append(m)

# TODO print the matrix
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=' ')
    print(end='\n')
