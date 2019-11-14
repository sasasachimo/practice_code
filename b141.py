S = input()
l = len(S)
cnt = 0
for i in range(l):
    if (i % 2 == 0 and (S[i] == 'R' or S[i] =='U' or S[i] =='D')) or (i % 2 != 0 and (S[i] == 'L' or S[i] =='U' or S[i] =='D')):
        cnt += 1
    else:
        cnt = 0
if cnt == l:
    print('Yes')
else:
    print('No')