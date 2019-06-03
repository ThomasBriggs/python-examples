def popRand(len, min, max):
    from random import randint as r
    array = []
    for i in range(len):
        array.append(r(min, max))
    return array

def popRand2(len, min, max):
    from random import randint as r
    list = range(min, max+1)
    n = (max-min) -1
    array = []
    for i in range(len):
        randInt = r(0, n)
        array.append(list[randInt])
        list.pop(randInt)
        n -= 1
    return array