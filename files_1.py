# f = open("demo.txt","r")          #f is handling the file in read mode
# print(f.read())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# f1 = open("demo1.txt","w")
# f1.write("This is a file ")

# myself = open("demo2.txt","w")
# myself.write("My name is Prateek Raj.\nI am persuing my btech in CSE from lovely professional university.")

# for i in f:
#     myself.write(i)



# try:
#     f = open("demo.txt")
    #your code goes here
# finally:    
#     f.close()
# This way we are making that file is closed properly even if exception is raised that cause the program to flow stop

# with open("demo.txt") as f:
#     f.read()  #----> example
    #your code goes here
    
f = open("demo.txt","r")    
print(f.read(10))
print(f.tell())
    