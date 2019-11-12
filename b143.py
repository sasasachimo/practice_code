N = int(input())
d = list(map(int, input().split()))
cmb = int(N * (N - 1) / 2)
cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        cnt = cnt + d[i] * d[j]
print(cnt)