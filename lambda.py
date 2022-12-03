# print even numbers
# def iseven(i):
#     return i%2==0
        
# list1 = [3,4,10,18,66,13,22,45]

# evenNum = list(filter(iseven,list1))
# print(evenNum)

#print numbers greater than 5
list1 = [1,3,5,6,12,9,35,12,23]
greater5 = list(filter(lambda i: i>5,list1))        #filter return the value that you required
print(greater5)

#square number
list1 = [1,3,5,6,12,9,35,12,23]
square = list(map(lambda i: i**2,list1))          #map goes to each element and perform the condition
print(square)

#triple the values of list
list1 = [1,3,5,6,12,9,35,12,23]
triple = list(map(lambda i : i*3,list1))
print(triple)

#upperlower
list1 = ["a","B","c","D","e","F"]
uplow = list(map(lambda i: i.swapcase(),list1 ))         #swapcase will swap the case from upper to lower and lower to upper
print(uplow)



def div(a,b):
    print(a/b)

def good_div(func):
    
    def inner_div(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner_div
div = good_div(div)
div(2,4)