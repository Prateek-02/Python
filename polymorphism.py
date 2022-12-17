# print(len("Hello"))
# print(len([10,20,30]))

# def add(x,y,z = 0):
#     return x+y+z
# print(add(3,4))
# print(add(3,4,5))


# class India:
#     def capital(self):
#         print("New Delhi")
#     def language(self):
#         print("Hindi")
#     def type(self):
#         print("Developing")
        

# class USA:
#     def capital(self):
#         print("Washington DC")
#     def language(self):
#         print("English")
#     def type(self):
#         print("Developed")        

# obj1 = India()
# obj2 = USA()

# for i in (obj1,obj2):
#     i.capital()
#     i.language()
#     i.type()  

# class Bird():
#     def wings(self):
#         print("birds have two wings")
#     def eyes(self):
#         print("birds have two eyes")   
#     def fly(self):
#         print("most of the birds can fly")         

# class Sparrow(Bird):    
#     def fly(self):
#         print("sparrow can fly")
        
# class Ostrich(Bird):    
#     pass
#     # def fly(self):
#     #     print("ostrich cannot fly")     
        
# bird = Bird()   
# sparrow = Sparrow()
# ostrich = Ostrich()
# sparrow = Sparrow()

# bird.eyes()
# bird.wings()
# bird.fly()
# ostrich.fly()
# sparrow.fly() 

#create a car class without any variables nad methods
# class car:
#     pass 

#create a child class Bus that will inherit all the variables and method of vehicle class

class vehicle:
    def __init__(self,name,milage):
        self.name = name
        self.milage = milage
        
class Bus(vehicle):
    pass

obj = Bus("ABC",12)
print(obj.milage,obj.name)        
                   
        
        