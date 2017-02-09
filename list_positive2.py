#list6.py

nums = [2,-4,5,-236,1,-2,7, 2, 4, -6]


newList = []
for x in xrange(0,len(nums)):
    if nums[x] > 0:
        newList.append(nums[x])
print (newList)
