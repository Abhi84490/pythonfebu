# a compnay decided to give bonus of 5% to empoye if his/her year of service is more than 5 years. ask user for theri salary and year of servise and print the net bonus amount

"""year = int(input("enter the year of service"))
salary = int(input("enter your salary"))
if year>5:
    print("bouns", (salary*5)/100)

else:
    print("no bouns",year, salary)
"""
""" """
# take values of length and breadth of a rectangle from user and check if it is squrare or not
"""len= int(input("enter the length: "))
bre = int(input("enter the breadth: "))
area= int(input("enter the area: "))
area_of_square= area**2
area_of_rectangle = len*bre

if area_of_square == area_of_rectangle:
    print("square")
else:
    print("not square")"""

#take three vlaues from user and print greates among them

"""first= int(input("enter the value1: "))
second = int(input("enter the value2: "))
third = int(input("enter the value3: "))
if first>second and first>second:
    print(first)
elif second>first and second>third:
    print(second)
elif third>first and third > second:
    print(third)"""
# a shop will give discount of 10% if the cost of purchased quantity is more than 10

item = 11
cost = 2000
if item>10:
    discount= (cost*10)/100
    print(discount)
else:
    print("no discount")