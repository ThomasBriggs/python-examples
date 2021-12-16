import numpy as np
import math

AMOUNT_OF_RUNS = 100000000

a1 = np.random.randint(0, 1000000, (AMOUNT_OF_RUNS))
a2 = np.random.randint(0, 1000000, (AMOUNT_OF_RUNS))

a = np.arange(10)

temp = np.gcd(a1, a2)
count = temp[temp == 1].shape[0]

print("Count: %s" % count)

temp = float(6 / (count / AMOUNT_OF_RUNS))
pi = math.sqrt(temp)
print("PI: {}".format(math.pi))
print("PI with Random: %s" % pi)

percentDif = ((math.pi - pi) / math.pi) * 100
print("Percentage Difference: {}%".format(percentDif))