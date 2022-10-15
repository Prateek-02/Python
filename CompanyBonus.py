#company will give bonus on following criteria
#time spent in company       Bonus
#greater than 10 years         10%

#more than 6 and less than 10    8%

#less than 6                     5%

#ask the salary and time spent from the user
#print the net bonus amount accordingly

salary = int(input("enter the salary:"))
year = int(input("enter the year spent:"))
if year > 10:
    bonus = salary*10/100
    print("salary after bonus is:" , salary + bonus)
if 6<year<10 :
    bonus = salary*8/100
    print("salary after bonus is:" , salary + bonus)
if year < 6:
    bonus = salary*5/100
    print("salary after bonus is:" , salary + bonus)  
    
    