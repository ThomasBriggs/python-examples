from random import randint


def init():
    numArray = range(randint(5, 20))
    return numArray


def populateRandom(inputArray, rangeOfValues):
    for x in range(len(inputArray)):
        inputArray[x] = randint(0, rangeOfValues)


def bubbleSort(inputArray, inverse=False):
    for i in range(len(inputArray) - 1, 0, -1):
        for j in range(i):
            if inverse == False:
                if inputArray[j] > inputArray[j + 1]:
                    temp = inputArray[j + 1]
                    inputArray[j + 1] = inputArray[j]
                    inputArray[j] = temp
            else:
                if inputArray[j] < inputArray[j + 1]:
                    temp = inputArray[j + 1]
                    inputArray[j + 1] = inputArray[j]
                    inputArray[j] = temp

    return inputArray


x = 0
while x < 1000:
    numArray = init()
    populateRandom(numArray, 999)
    print(bubbleSort(numArray))
    x+=1
