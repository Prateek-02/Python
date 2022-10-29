import random

b = (input("choose , rock paper scissor: "))
a = ["rock","paper","scissor"]
c = random.choice(a)
if b==c:
    print("tie")
elif b=="paper" and c=="scisscor":
    print("loss")
elif b=="rock" and c =="paper":
    print("loss")
elif b=="scissor" and c=="rock":
    print("loss")
else:
    print("win")                