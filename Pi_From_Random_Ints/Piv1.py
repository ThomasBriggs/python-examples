from random import randint as r
import math


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


AMOUNT_OF_RUNS = 100000000
MAX_RAND_INT = 1000000000000
count = float()

for i in range(AMOUNT_OF_RUNS):
    rand1 = r(0, MAX_RAND_INT)
    rand2 = r(0, MAX_RAND_INT)
    if gcd(rand1, rand2) == 1:
        count += 1

print("Count: %s" % count)

temp = float(6 / (count / AMOUNT_OF_RUNS))
pi = math.sqrt(temp)
print("PI: {}".format(math.pi))
print("PI with Random: %s" % pi)

percentDif = ((math.pi - pi) / math.pi) * 100
print("Percentage Difference: {}%".format(percentDif))
