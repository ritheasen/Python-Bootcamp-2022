
def matrix_multiplication(matrix1,matrix2):
    matrixMultiResult = [[0,0,0],
                        [0,0,0],
                        [0,0,0]]
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):

        for i in range (len(matrix1)):
            for j in range (len(matrix2)):
                for k in range (len(matrixMultiResult)):
                    matrixMultiResult[i][j] += matrix1[i][k] * matrix2[k][j]

        print(f"\nMatrix 1 :\n")
        for a in matrix1:
            print(str(a[0:])[1:-1].replace(","," "))
            
        print(f"\nMatrix 2 :\n")
        for b in matrix2:
            print(str(b[:])[1:-1].replace(","," "))

        print(f"\nThe result martix is :\n")
        for r in matrixMultiResult:
            print(str(r[0:])[1:-1].replace(","," "))

    else : 
        print(f"Error ! It may cause by your row of matrix 1 is not equal to the column of matrix 2")
    # print(f"Height matrix1 : {len(matrix1)}")
    # print(f"Width matrix1 : {len(matrix1[0])}")

    # print(f"Height matrix2 : {len(matrix2)}")
    # print(f"Width matrix2 : {len(matrix2[0])}")

matrix_multiplication([[3,7,5],
                        [2,6,7],
                        [4,3,2]],

                        [[6,5,4],
                        [3,2,1],
                        [1,2,3]])
    