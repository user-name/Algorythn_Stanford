import random
b=[]
for i in range(11):
    #print (i+1)/2
    b.append(i)
random.shuffle(b)
print b

c=sorted(b)
print c