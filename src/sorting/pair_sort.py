def sravnenie(A, B):
    if A[1] > B[1]:
        return True
    elif A[1] == B[1]:
        return A[0] < B[0]
    else:
        return False

def pair_sort():
    a=[]
    n=int(input())
    for z in range(n):
        a.append(list(map(int, input().split())))
    for i in range(len(a)):
        x=a[i]
        j=i-1
        while j>=0 and sravnenie(x,a[j]):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
    for x in a:
        print(*x)
        
if __name__ == '__main__':
    pair_sort()
