__author__ = 'Z'
f = open('HashInt.txt')  #otvet: 
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

"""

The goal of this problem is to implement a variant of the 2-SUM algorithm (covered in the Week 5 lecture on hash table applications)
The file contains 500,000 positive integers (there might be some repetitions!).This is your array of integers, with the ith row of the file specifying the ith entry of the array.

Your task is to compute the number of target values t in the interval [2500,4000] (inclusive) such that there are distinct numbers x,y in the input file that satisfy x+y=t. (NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 1501) in the space provided.

As an optional exercise, you might try implementing your own hash table for this question.

"""