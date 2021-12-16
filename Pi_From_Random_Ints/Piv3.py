import math
import numpy as np

total = 100000000


def inCircle(pos):
    return math.sqrt((pos[0] * pos[0]) + (pos[1] * pos[1])) < 1

a = np.random.uniform(0, 1, (total, 2))

inside = np.count_nonzero(np.array([inCircle(xi) for xi in a]))

print(f'inside: {inside}')

print(f'Pi: {(4*inside)/total}')
