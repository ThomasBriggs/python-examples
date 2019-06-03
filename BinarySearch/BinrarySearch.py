def bSearch(inputArray, target):

    found = False
    start = 0

    end = len(inputArray) -1

    while not found and start <= end:

        mid = (start + end)/2

        if inputArray[mid] < target:
            start = mid + 1

        elif inputArray[mid] > target:
            end = mid - 1

        elif inputArray[mid] == target:
            found = True
            return True

        elif start > end:
            return False
