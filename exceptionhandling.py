#try:
    #this block of code will run and throw errors if there is any

#except:
    #this will raise the error
    
#else:
    # this will execute if there are no errors

#finally:
    #this will execute regardless the result of try and except    
    
    
# try:
#     a = open("demo.py")
#     try:
#         a.write("abc")
#     except:
#         print("Error in file") 
#     finally:
#         a.close()
# except:
#     print("Error")               

# a = 5
# if a<10:
#     raise Exception("value is less than 10")

try:
	a = [1, 2, 3]
	print (a[3])
except LookupError:
	print ("Index out of bound error.")
else:
	print ("Success")

# a = [1,2,3]
# b = a[3]
# if b not in a:
#     raise Exception("index out of range")
