def rotateArray(arr, n, d):
	temp = []
	i = 0
	while (i < d):
		temp.append(arr[i])
		i = i + 1
	i = 0
	while (d < n):
		arr[i] = arr[d]
		i = i + 1
		d = d + 1
	arr[:] = arr[: i] + temp
	return arr

arr=[]
n=int(input("Number of elements in array:"))
for i in range(0,n):
   l=int(input())
   arr.append(l)
print("Array after left rotation is: ", end=' ')

d = int(input("Rotation size"))
print(rotateArray(arr, n , d))

