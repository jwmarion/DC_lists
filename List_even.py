#list4.py

nums = [2,4,5,236,1,2,7, 2, 4, 6]
nums.sort()
print("Even numbers in list: ")

for x in xrange(0,len(nums)):
    if nums[x] % 2 == 0:
        print nums[x]
