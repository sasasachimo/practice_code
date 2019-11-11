s = [input() for i in range(2)]
cnt = 0
for i in range(3):
    if s[0][i] == s[1][i]:
        cnt = cnt + 1
print(cnt)
