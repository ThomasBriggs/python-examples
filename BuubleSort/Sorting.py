def iSort(input):

    n = len(input)

    for i in range(1,  n):
        temp = input[i]
        j = i

        while j > 0 and input[j-1]>temp:
            input[j] = input[j - 1]
            j -= 1

        input[j] = temp

def bSort(input):
    for i in range(len(input)):
        for j in range(len(input)-i-1):
            if input[j] > input[j+1]:
                temp = input[j]
                input[j] = input[j+1]
                input[j+1] = temp