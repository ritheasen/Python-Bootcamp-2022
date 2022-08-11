def matrix_addition(matrix1,matrix2):
    print(f"\nMatrix 1 :\n")
    for a in matrix1:
        print(str(a[0:])[1:-1].replace(","," "))
        
    print(f"\nMatrix 2 :\n")
    #print(str(matrix2[:])[1:-1].replace("["," ").replace("]","").replace(","," "),sep="\n")

    for b in matrix2:
        print(str(b[:])[1:-1].replace(","," "))

    #print("\n","Matrix 1:","\n",*matrix1,sep="\n") 
    #The * in front of the matrix makes the contents of the list individual arguments .
    #sep is ‘\n,’ i.e., newline, the list’s value is printed in a new line every time.
    #print("\n", "Matrix 2:","\n",*matrix2,sep="\n".replace("[","").replace("]",""))
    #print(*matrix2,str(matrix2[0:])[1:-1].replace("[","").replace("]",""),sep="\n")
    matrixAddition = [[matrix1[i][j] + matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    print(f"\nThe result martix is :\n")
    for r in matrixAddition:
        print(str(r[0:])[1:-1].replace(","," "))
        #print(r)

matrix_addition([[10,5,4,2],
                [5,0,9,5],
                [9,19,60,8],
                [7,8,4,5]],

                [[12,65,34,42],
                [10,5,89,45],
                [11,21,63,78],
                [87,78,54,65]])