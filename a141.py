s = input()
l = ['Sunny', 'Cloudy', 'Rainy']
for i in range(3):
    if s == l[i]:
        num = i
if num == 2:
    ans = l[0]
else:
    ans = l[num + 1]
print(ans)
