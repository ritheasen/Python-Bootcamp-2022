import random

tupleLength = int(input("Enter length of random number in Tuple"))
newTuple = []

def random_tuple(nTime):
    print(f"random_tuple({tupleLength})")
    sum = 0
    for i in range(1,nTime+1):
        randoM = random.randint(0, 100)
        print(f"Random number {i}:{randoM}")
        newTuple.append(randoM)
        sum += randoM
    print(tuple(newTuple))
    #print(sum(newTuple))
    print(sum)
    return sum
random_tuple(tupleLength)