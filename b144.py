n = int(input())
for A in range(1,10):
    if n % A == 0:
        B = n / A
        if 1 <= B <= 9:
            ans = "Yes"
        else:
            ans = "No"
print(ans)
