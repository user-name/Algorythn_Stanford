__author__ = 'Z'
f = open('Median.txt')  #otvet: 1213
#f = open('med.txt') #otvet: 1666
#f = open('med2.txt') #otvet: 4758
#f = open('med3.txt') #otvet: 4011
array_of_integer=[]
result=0
for line in f:
    array_of_integer.append(int(line))
    a=sorted(array_of_integer)
    position=((len(a)+1)/2)-1 #position of median element
    result+=a[position]
print result
