def bubble_sort():
	n=int(input())
	z=input()
	a=z.split(' ')
	for i in range(n-1):
		for j in range(n-i-1):
			if a[j]>a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
				print(' '.join(map(str, a)))
if __name__ == "__main__":
	bubble_sort()
