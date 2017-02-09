#list9.py

mat1 = [[1,2], [3,4]]
mat2 = [[5,6],[7,8]]
mat3 = []

for x in xrange(0,2):
    for y in xrange(0,2):
        mat3.append(mat1[x][y]+mat2[x][y])


result = [[mat3[0],mat3[1]],[mat3[2],mat3[3]]]
print result
