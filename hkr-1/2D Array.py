import sys
n = []
m=[]
for n_i in range(0,6):
    n.append(map(int,raw_input().strip().split(' ')))
for t in xrange((len(n)-2)):
    for s in xrange((len(n[t])-2)):
        m.append(n[t][s:s+3]+[n[t+1][s+1]]+n[t+2][s:s+3])
print sum(max(m,key=lambda x: sum(x)))
