#print area of triangle using heron's formula
import math
a,b,c = 6,2,6
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print('area of triangle:',a,b,c)
print('area:',area,'square units')

