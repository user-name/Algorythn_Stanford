__author__ = 'Z'
#f = open('HashInt.txt')
f = open('2sum.txt')
array_of_integer=[]

for line in f:
    array_of_integer.append(int(line))

set_of_integer=set(array_of_integer)
result=set()
res=0
#for t in array_of_integer[2499:4000]:
for t in range(2500,4001):
    for i in array_of_integer:
        r=t-i
        #if r>0 and r!=i and (r in set_of_integer):
        if r>0 and (r in set_of_integer):
            result.add(i)
            res+=1
print len(result)
print res
