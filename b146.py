N = int(input())
S = input()
L = [chr(i) for i in range(65, 65+26)]
ans = ''
for i in range(len(S)):
    A = (L.index(S[i])+N) % 26
    ans += L[A]
print(ans)