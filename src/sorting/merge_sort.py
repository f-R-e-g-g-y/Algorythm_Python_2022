def merge(A, B):
    a=[]
    x=0
    y=0
    while x < len(A) and y < len(B):
        if A[x] <= B[y]:
            a.append(A[x])
            x += 1
        else:
            a.append(B[y])
            y += 1
    a += A[x:]
    a += B[y:]
    return a

def merge_sort(A, nach, konec):
    if (konec - nach) == 1:
        return A[nach:konec]
    centr = int((nach + konec) / 2)
    left = merge_sort(A, nach, centr)
    right = merge_sort(A, centr, konec)
    z = merge(left, right)
    print(nach + 1, konec, z[0], z[-1])
    return z

n = int(input())
print(*merge_sort(list(map(int, input().split())), 0, n))
