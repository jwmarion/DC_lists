#list5.py

nums = [2,-4,5,-236,1,-2,7, 2, 4, -6]
nums.sort()
print("Positive numbers in list: ")

for x in xrange(0,len(nums)):
    if nums[x] > 0:
        print nums[x]
