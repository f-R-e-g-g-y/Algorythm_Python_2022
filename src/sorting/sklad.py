def sklad():
    n = int(input())
    tovar = list(map(int, input().split()))
    n1 = int(input())
    zakaz = list(map(int, input().split()))
    a = [0] * max(zakaz)
    for item in zakaz:
        a[item - 1] += 1
    for i in range(len(tovar)):
        if tovar[i] >= a[i]:
            print('no')
        else:
            print('yes')
            
if __name__ == '__main__':
    sklad()
