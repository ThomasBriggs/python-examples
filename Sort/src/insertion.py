
a = [80, 29, 12, 16, 40, 93, 6, 14, 9, 3]

def swap(arr, index1, index2):
	temp = arr[index1]
	arr[index1] = arr[index2]
	arr[index2] = temp

for i in range(0, 10):
	j = i
	while(j > 1 and a[i] < a[i-1]):
		swap(a, i, i-1)
		j -= 1

print(a)
