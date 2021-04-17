# class Introduction:
#     pass
# obj=Introduction()
# print(dir(obj))
# class Calculate:
#     def take_value(self):
#         principal=int(input("Enter the amount:"))
#         time=int(input("Enter time in years:"))
#         rate=int(input("Enter the rate:"))
#         return [principal,time,rate]
#     def calculate(self):
#         ptr=self.take_value()
#         simple_interest=ptr[0]*ptr[1]*ptr[2]/100
#         return simple_interest
#     def display(self):
#         print("The required simple interest is ",self.calculate())
# obj = Calculate()
# obj.display()
# class Introduction:
#     total_emp=0
#     def __init__(self,emp_name):
#         Introduction.total_emp+=1
#     def getTotalEmp(self):
#         return self.total_emp
# obj=Introduction('ram')
# obj1=Introduction('sita')
# obj2=Introduction('sophia')
# obj3=Introduction('hari')
# print(obj.getTotalEmp())
# class Introduction:
#     def test(self):
#         print("Hello")
# x=((Introduction().test()))