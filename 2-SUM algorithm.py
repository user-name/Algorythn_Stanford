__author__ = 'Z'
f = open('HashInt.txt')  #otvet: 1477
#f = open('2sum.txt') #otvet: 1453
array_of_integer=[]

for line in f:
    array_of_integer.append(int(line))

set_of_integer=set(array_of_integer)
result=set()

#for t in array_of_integer[2499:4000]:
for t in range(2500,4001):
    for y in array_of_integer:
        x=t-y
        #if r>0 and r!=i and (r in set_of_integer):
        if x>0 and x!=y and (x in set_of_integer):
            result.add(t)
            #print result
            #print t, y, "x = ",x, "/n"

print len(result)

