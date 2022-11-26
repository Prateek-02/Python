#tuples are ordered
#tuples are immutable
#it allowes duplicate values
#tuples are order

# mytuple = ("apple","orange","grapes")
# print(mytuple)
# print(len(mytuple))

# mytuple = ("apple","orange","grapes")
# print(mytuple[0])

# mytuple = ("car","bike","train","boat")
# mylist = list(mytuple)
# mylist.append("1")
# #mylist.pop()
# print(mylist)

# tuple1 = (1,2,3)
# tuple2 = (4,5,6)
# tuple1 += tuple2
# print(tuple1)

# tuple1 = (1,2,3)
# del tuple1
# print(tuple1)

# tuple1 = (1,2,3,4,5)
# mylist = list(tuple1)
# mylist.reverse()
# tuple2 = tuple(mylist)
# print(tuple2)

# name = ("Prateek",)
# print(name)


# tuple1 = ("A","B","C",)
# (one,two,three) = tuple1
# print(one)   # output - A
# print(two)    # output - B
# print(three)    # output - C


# tuple1 = (10,20,30,40)
# (a,b,c,d) = tuple1
# print(a)
# print(b)
# print(c)
# print(d)

#swap tuples
# tuple1 = (10,20)
# tuple2 = (30,40)
# tuple3 = tuple2   #tuple3=(30,40)
# tuple2 = tuple1   #tuple2=(10,20)
# tuple1 = tuple3   #tuple1=(30,40)
# print(tuple1)
# print(tuple2)
# tuple1,tuple2 = tuple2,tuple1  #tupple swapped 
# print(tuple1)                  #(10,20)
# print(tuple2)                  #(30,40)

#loops
#tuple1 = ("car","boat","bike")
#  for i in tuple1:
#      print(i)

# i = 0
# while i<len(tuple1):
#     print(tuple1[i])
#     i = i+1


tuple1 = (1,[6,7],2,3,4,5)
# print(tuple1[1][0])   #6
# print(tuple1[1][1])   #7
list1 = list(tuple1)   #[1,[6,7],2,3,4,5]
list1[1][0]=8          #[6,7][6] = [8]
print(list1)           #[1,[8,7],2,3,4,5]
