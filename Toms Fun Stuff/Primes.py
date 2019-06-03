def isPrime(test_num):
    notPrime = False
    for i in range(1, test_num):
        if i != 1 and test_num % i == 0:
            notPrime = True
    if not notPrime:
        return True
    else:
        return False


def primeGen(min, max=False):
    if max == False:
        max = min
        min = 0
    prime_list =[]
    for i in range(min, max+1):
        if isPrime(i):
            prime_list.append(i)
    return prime_list