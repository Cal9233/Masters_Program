
def bubbleSort(a):
	for i in range(len(a)):
		for j in range(0, len(a)-i-1):
			if a[j] > a[j+1]:
				a[j+1], a[j] = a[j], a[j+1]
		for k in range(len(a)-1, len(a)-(i+2), -1):

			print(f"a[k]: {a[k]}")
			print(f"a[k-1]: {a[k-1]}")
			if (a[k] < a[k-1]):
				print(f"Error at i = {i}")
				break
			
data = [15, -3, -9, 3, 16, 0]
bubbleSort (data)
print (data)