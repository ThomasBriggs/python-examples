import math
def convert_bin(a):
    if a == 0:
        return [0]
    num = a
    start_bit = 2 ** (math.floor(math.log(a,2)))
    current_bit = start_bit
    bin_array = []
    while current_bit >= 1:
        if (a - current_bit >= 0):
            bin_array.append(1)
            a = a- current_bit
        else:
            bin_array.append(0)
        current_bit = current_bit / 2
    return bin_array

a = 31
b = 0
a_bin = convert_bin(a)
b_bin = convert_bin(b)

n = len(a_bin)
if len(b_bin) > n:
    diff = len(b_bin) - len(a_bin)
    for i in range(diff):
        a_bin.insert(0, 0)
else:
    diff = len(a_bin) - len(b_bin)
    for i in range(diff):
        b_bin.insert(0, 0)

print(a_bin)
print(b_bin)

changes = 0

for i in range(len(a_bin)):
    if a_bin[i] != b_bin[i]:
        changes += 1

print(changes)