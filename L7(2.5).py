# і рядки, j стовпці
n=int(input("Enter n = "))
c = [ [ float(input(' Enter c[{0}][{1}]='.format(i,j))) for j in range(n)] for i in range(n)]
print('c = {0}'.format(c))
matrix = []
el=0
k=1
b1=1
b=[]

for i in range(n):
    r = []
    for j in range(n):
        if (i+j) % 2 == 0:
            for k in range(1,n+1):
                el +=k
        if (i+j)%2!=0:
            for k in range(1,n + 1):
                el +=k**2
        r.append(el)
    matrix.append(r)
print('matrix = {0}'.format(matrix))
for j in range(n):
    dob = 1
    for i in range(n):
        dob *= matrix[i][j]
    b.append(dob)
print('b ={0} '.format(b))
