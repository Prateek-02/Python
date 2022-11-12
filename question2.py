def add (a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
print("1. Add")
print("2. subtract")
print("3. multiply")
print("4. divide")
choice = input("enter choice(1/2/3/4): ")
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
if choice == "1":
    print(a,"+",b,"=",add(a,b))
elif choice == "2":
    print(a,"-",b"=",sub(a,b))
elif choice == "3":
    print(a,"*",b"=",multi(a,b))
elif choice == "4":
    print(a,"/",b"=",div(a,b))   
        
    