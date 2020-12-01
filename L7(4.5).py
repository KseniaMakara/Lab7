n = int(input('n = '))
A = [[float(input('A[{0}][{1}]='.format(i,j))) for j in range(n)] for i in range(n)]
print(A)
b = []
for i in range (n):
    for j in range(n):
        if i%2==0:
            b.append(A[i][j])
print('b = {0}'.format(b))
c=sorted(b, reverse=True)
print('c = {0}'.format(c))

