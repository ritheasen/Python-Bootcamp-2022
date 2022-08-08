from multiprocessing.connection import answer_challenge


def binary_multiplication(decimal1,decimal2):

    binary1 = bin(int(decimal1)).replace("0b","")
    binary2 = bin(int(decimal2)).replace("0b","")

    # firstnumber = 110
    # secondnumber = 10
  
    # firstnumber = str(firstnumber)
    # secondnumber = str(secondnumber)
  
    binaryMultiply = int(binary1, 2) * int(binary2, 2)
    answerToBinary = bin(binaryMultiply).replace("0b","")
  
    print(f"binary_addition({decimal1},{decimal2})")
    print("Num1 : ",binary1)
    print("Num2 : ",binary2)

    
    print(f"Sum(Binary) : {answerToBinary}")
    
    print(f"Sum(Decimal) : {binaryMultiply}")

binary_multiplication(60,50)


    