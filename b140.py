N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
score = 0

for i in range(N):
    j = A[i] - 1
    if i > 0 and A[i] - A[i-1] == 1:
        score += B[j] + C[j-1]
    else:
        score += B[j]
print(score)