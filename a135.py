i = list(map(int, input().split()))
if (i[0] - i[1]) % 2 == 0:
  print(min(i[0],i[1]) + abs(i[0] - i[1]) // 2)
else:
  print("IMPOSSIBLE")
