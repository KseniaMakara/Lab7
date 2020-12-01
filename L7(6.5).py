n = int(input('n = '))
a = [[float(input('A[{0}][{1}]='.format(i,j))) for j in range(n)] for i in range(n)]
b = []
for j in range(1, n+1):
    z = []
    for k in range(j):
        z.append(a[n-k-1][n-j+k])
    b.append(z)
    z = []
    for k in range(j):
        z.append(a[j-k-1][k])
    b.append(z)
d = [a[i][n-i-1] for i in range(n)]
d.reverse()
b.remove(d)
b.remove(d)
print(b, '\n\n')
for m in range(len(b)):
    b[m] = sum([abs(el) for el in b[m]])
print(b)
print(min(b))