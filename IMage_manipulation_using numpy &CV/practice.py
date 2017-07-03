L=[1,2,3]
L.append(4)
L=L+[5]
print(L)
P=[1,2,3,4,5]
G=[]
for i,j,k in zip(L,P,range(0,5)):
    G.append(i+j)
T = 1000000
for t in xrange(T):
    print(t)
