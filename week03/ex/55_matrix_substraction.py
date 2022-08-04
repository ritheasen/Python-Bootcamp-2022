def matrix_subtraction(matrix1,matrix2):

    print(f"\nMatrix 1 :\n")
    for a in matrix1:
        print(str(a[0:])[1:-1].replace(","," "))
        
    print(f"\nMatrix 2 :\n")
    for b in matrix2:
        print(str(b[:])[1:-1].replace(","," "))

    matrixAddition = [[matrix1[i][j] - matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    print(f"\nThe result martix is :\n")
    for r in matrixAddition:
        print(str(r[0:])[1:-1].replace(","," "))

matrix_subtraction([[10,5,4,2],
                [5,10,9,55],
                [9,19,69,8],
                [7,8,4,75]],

                [[12,65,34,2],
                [1,5,8,45],
                [7,21,63,8],
                [0,78,4,65]])