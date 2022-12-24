import re

value = "this is a string"
output = re.search("^this  .*strings", value)
print(output)

pattern =  r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"

print(pattern)
#r = raw