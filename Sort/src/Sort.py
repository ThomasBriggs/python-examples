def genRandom(x, min=0, max=100):
    from random import randint
    a = []
    for i in range(x):
        a.append(randint(min, max))
    return(a)

def bubbleSort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return(array)
