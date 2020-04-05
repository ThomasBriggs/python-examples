global A
global count1
global count2

count1 = 0
count2 = 0


def quicksort(first, last):
    if first < last:
        pivot = A[first]
        left = first + 1
        right = last
        while left <= right:
            while left <= right and A[right] >= pivot:
                right -= 1
            while left <= right and A[left] <= pivot:
                left += 1
            if left <= right:
                swap1(left, right)  # Swap 1
        swap2(first, right)  # Swap 2
        splitPoint = right
        quicksort(first, splitPoint - 1)
        quicksort(splitPoint + 1, last)


def swap1(index1, index2):
    temp = A[index1]
    A[index1] = A[index2]
    A[index2] = temp
    count1 += 1


def swap2(index1, index2):
    temp = A[index1]
    A[index1] = A[index2]
    A[index2] = temp
    count2 += 1


count1 = 0
count2 = 0
A = [23, 12, 16, 13, 1, 5, 22, 2]
print(A)
quicksort(0, 7)
print(A)

print(count1)
print(count2)
