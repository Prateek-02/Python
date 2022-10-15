# A company decided to give bonus of Rs1000 to 
#employee of his/her service is more than 5 years
#ask user their salary and year of service and print
#the net bonus amount

salary = int(input("enter the salary amount :"))
year = int(input("enter the year of service:"))
if year >= 5 :
    print("He/She is eligible for the bonus of Rs1000")
    print("salary afrer bonus is Rs:" , salary + 1000)
else :
    print("He/She is not elegible")    