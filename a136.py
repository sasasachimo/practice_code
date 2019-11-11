i = list(map(int, input().split()))
n = i[2] - (i[0] - i[1])
if n > 0:
    print(n)
else:
    print(0)
