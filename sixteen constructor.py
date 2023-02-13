#  # constructor
#
# # class std:
# #      def details(self,name,age, marks):
# #          return name
# #          return age
# #          return marks
# # s=std()
# # print(s.details("a",34, 4444))
# # print(s)
#
# # class std:
# #      def details(self, name, age, marks):
# #          print(name)
# #          print(age)
# #          print(marks)
# #
# #
# # s = std()
# # s.details("a", 34, 4444)
# # # print(s)
#
# class std:
#     def details(self,name,age,marks):
#         return name,age,marks
# s=std()
# s.details("a",23,455534)
# # print(s.details)

                                # CONSTRUCTOR
#
# class std:
#     def __init__(self, name, age):
#
#         self.name= name
#         self.age=age
# s=std("abcd",98)
# s.name
# print(s.name)
# # init= initilizer


# inheritance
# class emp1:
#     def __init__(self, name,sal):
#         self.name=name
#         self.sal=sal
#
# class emp2(emp1):
#     def __init__(self,name,sal,age):
#         emp1.__init__(self, name, sal)
#
#         self.age = age
#
# e = emp2("kartik",20,3000)
# e.age
# e.name
# print(e.age, e.name)


# wap to check the speed of a bike using oops fundaments where the distance is convered by bike is almost 250km and time taken is
# 10 hours.
# class bike:
#     def __init__(self,distance, time):
#         self.distance = distance
#         self.time= time
#         # self.speed = distance/time
#     def speed(self):
#         speed = self.distance/self.time
#         print(speed)
# a= bike(250,10)
# print(a.speed())
# wap to find the sal of a two emp ram and shyam where ram take 4 leaves in a month with a deduction of 5.6% of the salary while shyam take no leave with the
# increment of 30% help of oops fundamental

# ram = int(input("enter your salary: "))


# wap to perform inheritance and find the avg marks and std 2
# class std1:
#     def __init__(self, eng, hindi):
#         self.eng=eng
#         self.hindi = hindi
#
# class std2(std1):
#     def __init__(self,eng, hindi):
#         std1.__init__(self,eng, hindi)
#
#     def avg(self):
#         a= (self.eng+ self.hindi)/2
#         return a
# s= std2(23,343)
# print(s.avg())

# class std1:
#     def __init__(self,eng,hindi):
#         self.eng=eng
#         self.hindi=hindi
#
# class std2:
#     def __init__(self,eng,hindi):
#         super().__init__ (eng,hindi)
#     def avg(self):
#         a= (self.eng+self.hindi)/2
#         return a
# s=   std2(23,34)
# print(s.avg())

# multilevel inheritance
class gpc:
    def __init__(self,name):
        self.name = name
class pc(gpc):
    def __init__(self,age):
        super().__init__(age)
        self.age = age
class cc:
    def __init__(self,sal):
        self.sal=sal
p=pc('asd',98)
print(p.name())