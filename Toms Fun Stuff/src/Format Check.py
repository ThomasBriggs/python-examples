def formatCheck(format, input):
    formatArray = []
    for i in format:
        formatArray.append(i)
    j = 0
    check = True
    for i in input:
        if formatArray[j] == "N":
            subCheck = False
            for n in range(10):
                if formatArray[j] == n:
                    subCheck = True
            if subCheck == False:
                check = False
        elif formatArray[j] != i:
            check = False
        j += 1
    return check