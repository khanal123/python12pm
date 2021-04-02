# def test():
#     print("Hello")
# # print(test)
# print(test())
# def pr(data):
#     print(data)
# pr("Hello")
# def add(x,y):
#     return x+y
# print(add(11,3))
# def introduction(name,age=0):
#     print(f"Hello {name}")
#     if age>0:
#         print(age)
# introduction('ram',30)
# def sum_sub(a, b):
#     sum=a+b
#     sub=a-b
#     return [sum,sub]
# get=sum_sub(2,4)
# # print(get)
# print(get[0])
# print(get[1])
# def take_value():
#     principal = int(input("Enter the amount:"))
#     rate = float(input("Enter the rate:"))
#     time = int(input("Enter the time:"))
#     return [principal, rate, time]
# def calculate():
#     data = take_value()
#     simple_interest = data[0] * data[1] * data[2] / 100
#     return simple_interest
# def display():
#     print(f"Simple interest is {calculate()}")
# display()
# def connection():
#     """
#     database connection function
#     """
#     return "database was connected"
# print(connection.__doc__)
# x=10
# def test():
#     global x
#     x=30
#     x=x+20
#     print(x)
# test()
#Anonymous function
# simple_interest=lambda p,t,r:p*t*r/100
# # a=int(input("Enter p:"))
# print(simple_interest(10,3.5,4))
# def test():
#     def get(name):
#         return f"Hello {name}"
#     return get
# a=test()
# print(a('ram'))
# #print(test()('ram'))
# import database
# print(database.insert())
# from database import insert as data_insert
# from datatypes import insert
# print(insert())
# print(data_insert())
from lib import *
print(database.insert())
print(students.get_student())