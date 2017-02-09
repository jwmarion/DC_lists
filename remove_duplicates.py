#list11.py



#Given an list of numbers or strings,
#create a new list containing the same elements as
#the first list, except with any duplicate values removed. Print the list.

oList = [1,2,3,4,5,6,7,8,8,8,7,7,6,6]
rList = []
for x in xrange(0,len(oList)):
    if (oList[x] in rList) == False:
        rList.append(oList[x])
print rList
