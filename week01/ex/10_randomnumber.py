import random

nInput = int(input("Input Number: "))
sum = 0

for i in range (0,nInput):
    randomNumber = random.randint(2000, 3000)
    sum += randomNumber
print(f"Sum of even random numbers: {sum}")
