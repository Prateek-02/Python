#def hello():
#    print("hello world")
#    print("good noon")
#hello()    

#def hello_world():
#    print("hello world")

#def hello_mars():
#    print("hello mars")
    
#hello_world()        
#hello_mars()

#def name(x):
#    print(x)
#name(4)  
#name(10)  

#def add(num1,num2):
#    sum = num1 + num2
#    print(sum)
#add(5,10)    
#add(2,8)
#add(9,10)

"""def  sub(num1,num2):
    diff = num1 - num2
    print(diff)
sub(10,8)
sub(17,9)""" 

"""def multi(num1,num2):
    product = num1 * num2
    return product

result1 = multi(2,4)
result2 = multi(9,10)
print(result1,result2)"""

"""def name(myname):
    print("my name is: " + myname)
    
name("Prateek")""" 

"""def name(firstname, lastname):
    print("My name is: " + firstname + ' ' + lastname)
    
name("Prateek","Raj")"""          

"""def name(firstname = "Prateek"):
    print("My name is: ", firstname)
    
name()
name("Kohli")
name("Rohit")    
name("Dhoni")"""

"""def name(firstname,age):
    print("My name is: ",firstname)
    print("My age is: ",age)
name("Prateek",19)"""

"""def employee(name, salary = 10000):
    print(name + str(salary))
employee("Ben: ",12000)
employee("Mike: ",15000)
employee("Bob: ")  """

"""def details(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
details("Prateek",place = "Giridih",age = 19,number = 99999999)"""


"""a = 10

def func():
    global a
    print(a)
func()
print(a)"""

"""import sys
sys.setrecursionlimit(100)
def hello():
    print("Hello world")
    hello()
hello()"""

"""def sum_recursion(num):
    if num == 0:
        return num
    return num+sum_recursion(num-1)
ans = sum_recursion(5)
print(ans)"""

def factorial(num):
    if num == 0:
        return 1
    return num*factorial(num-1)
ans = factorial(5)
print(ans)
    

   
 
        