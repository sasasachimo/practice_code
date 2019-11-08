s = list(map(int, input().split()))
ans = 0
if s[0] < 10 and s[1] < 10:
    ans = s[0] * s[1]
else:
    ans = - 1
print(ans)