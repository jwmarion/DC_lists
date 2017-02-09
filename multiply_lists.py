#list8.py

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
res = []

for x in xrange(0,len(nums1)):
    res.append(nums1[x]*nums2[x])

print res
