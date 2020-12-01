n = int(input('n = '))
a = [list(map(float, input().split())) for i in range(n)]
b = []
for j in range(n):
    if len([a[i][j] for i in range(n) if a[i][j] >= 0]) == n:
        b.extend([a[i][j] for i in range(n)])
s = sum(b)
print(s)