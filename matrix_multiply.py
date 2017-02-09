#list12.py
max1 = [[1,2],[3,4]]
max2 = [[5,6],[7,8]]
maxr = [[0,0],[0,0] ]

for x in xrange(0,2):
    for y in xrange(0,2):
        for z in xrange(0,2):
            maxr[x][y] += max1[x][z] * max2[z][y]
print maxr
