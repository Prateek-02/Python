import math
a,b,c = 10,8,7
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**1/2
print('sides of triangle: ', a,b,c)
print('area:' ,area,"square units")