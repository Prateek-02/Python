class A:                                          #parent class
    def __init__(self):
        print("Init of class A")
        
    def method1(self):
        print("this is method1")
    def method2(self):
        print("this is method2")    


class B():                                          #child class
    def __init__(self):
        # super.__init__()                          #by using "super" we can call the parent class
        print("Init of class B")                  
    def method3(self):
        print("this is method3")
    def method4(self):
        print("this is method4")

class C(B,A):                                     #child class
    def __init__(self):
        super().__init__()
        print("Init of class C")
    def method5(self):
        print("this is method5")
                
obj = C()
obj.method1 