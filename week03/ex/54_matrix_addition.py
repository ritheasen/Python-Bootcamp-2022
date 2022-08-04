def matrix_addition(matrix1,matrix2):
    
    print(f"\nMatrix 1 :\n")
    for a in matrix1:
        print(str(a[0:])[1:-1].replace(","," "))
        
    print(f"\nMatrix 2 :\n")
    for b in matrix2:
        print(str(b[:])[1:-1].replace(","," "))

    matrixAddition = [[matrix1[i][j] + matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    print(f"\nThe result martix is :\n")
    for r in matrixAddition:
        print(str(r[0:])[1:-1].replace(","," "))

matrix_addition([[10,5,4,2],
                [5,0,9,5],
                [9,19,60,8],
                [7,8,4,5]],

                [[12,65,34,42],
                [10,5,89,45],
                [11,21,63,78],
                [87,78,54,65]])