import sys
from _datetime import datetime

curTime = datetime.now()

name = input("Enter your name\n")
age = int(input("Enter your age\n"))

hundredYears = (curTime.year - age) + 100


print(name + ", you are gonna be 100 years old in year: " + hundredYears.__str__())