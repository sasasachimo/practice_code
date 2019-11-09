s = list(map(int, input().split()))
A = s[0]
B = s[1]
if A >= B * 2:
    ans = A - B * 2
else:
    ans = 0
print(ans)
