#list10.py
mat1 = [[1,2,5,1,1,1], [3,4,6,1,1,1], [1,2,3,1,1,1]]
mat2 = [[5,6,4,1,1,1],[7,8,11,1,1,1],[1,2,3,1,1,1]]
mat3 = []

len1 = len(mat1)
len2 = len(mat1[0])

for x in xrange(0,len1):
    for y in xrange(0,len2):
        val =0;
        val += mat1[x][y]+mat2[x][y]
        mat1[x][y]=val

print mat1
