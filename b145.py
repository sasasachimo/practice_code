N = int(input())
S = input()
T = int(N/2)
if len(S) % 2 == 1:
    print('No')
elif S[:T] == S[T:]:
    print('Yes')
else:
    print('No')