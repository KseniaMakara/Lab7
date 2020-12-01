n=int(input('n = '))
m=int(input('m = '))
a = [[float(input('a[{0}][{1}]='.format(i,j))) for j in range(m)] for i in range(n)]
print(a)
r=[]
s = 0
for i in range(n):
    for j in range(m):
        if i%2==0 and  j%2==0 and a[i][j]<0:
            s+=a[i][j]
print(s)